import os
import re
import csv


apis = [
    "torch.add",
    "torch.addmm",
    "torch.exp",
    "torch.matmul",
    "torch.mm",
    "torch.mul",
    "torch.relu",
    "torch.sigmoid",
    "torch.softmax",
    "torch.tanh",
]


output = "results/summary_60s.csv"


rows = []


for api in apis:

    path = f"results/raw_logs/{api}/fuzz_result.txt"

    if not os.path.exists(path):
        print("Missing:", api)
        continue


    text = open(path).read()


    def extract(pattern):
        m = re.search(pattern, text)
        return m.group(1) if m else "NA"


    rows.append([
        api,
        extract(r"stat::number_of_executed_units:\s+(\d+)"),
        extract(r"stat::average_exec_per_sec:\s+(\d+)"),
        extract(r"stat::new_units_added:\s+(\d+)"),
        extract(r"stat::peak_rss_mb:\s+(\d+)")
    ])



with open(output,"w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "API",
        "executed_units",
        "exec_per_sec",
        "new_units_added",
        "peak_rss_mb"
    ])

    writer.writerows(rows)


print("saved:",output)
