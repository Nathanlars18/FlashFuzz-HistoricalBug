#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def parse_log(log_path: Path):
    result = {
        "rounds": 0,
        "invalid": 0,
        "cpu_error_count": 0,
        "valid": 0,
        "validity_ratio": 0,
        "statistics_status": "OK",
        "stat_entry_count": 0,
        "done_entry_count": 0,
    }

    if not log_path.exists():
        result["statistics_status"] = "INCOMPLETE"
        result["reason"] = "missing_fuzz_log"
        return result

    text = log_path.read_text(errors="replace")

    stat_matches = re.findall(r"stat::number_of_executed_units:\s*(\d+)", text)
    done_matches = re.findall(r"^Done\s+(\d+)\s+runs", text, flags=re.MULTILINE)

    result["stat_entry_count"] = len(stat_matches)
    result["done_entry_count"] = len(done_matches)
    result["invalid"] = text.count("Exception caught:")
    result["cpu_error_count"] = text.count("CPU Execution error")

    reasons = []

    if len(stat_matches) == 1:
        result["rounds"] = int(stat_matches[-1])
        result["round_source"] = "stat"
    elif len(stat_matches) > 1:
        result["rounds"] = int(stat_matches[-1])
        result["round_source"] = "stat"
        result["statistics_status"] = "INCONSISTENT"
        reasons.append("multiple_stat_entries")
    elif len(done_matches) == 1:
        result["rounds"] = int(done_matches[-1])
        result["round_source"] = "done"
    elif len(done_matches) > 1:
        result["rounds"] = int(done_matches[-1])
        result["round_source"] = "done"
        result["statistics_status"] = "INCONSISTENT"
        reasons.append("multiple_done_entries")
    else:
        result["statistics_status"] = "INCOMPLETE"
        reasons.append("missing_round_information")

    if result["rounds"] > 0:
        result["valid"] = result["rounds"] - result["invalid"]
        result["validity_ratio"] = round(result["valid"] / result["rounds"], 6)

        if result["invalid"] > result["rounds"]:
            result["statistics_status"] = "INCONSISTENT"
            reasons.append("invalid_exceeds_rounds")
    else:
        result["valid"] = 0
        result["validity_ratio"] = 0

    if reasons:
        result["reason"] = ";".join(reasons)

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_dir", required=True, help="Directory containing fuzz-0.log")
    args = parser.parse_args()

    log_dir = Path(args.log_dir)
    log_path = log_dir / "fuzz-0.log"

    result = parse_log(log_path)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
