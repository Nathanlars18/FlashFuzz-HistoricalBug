#!/usr/bin/env python3

import os
import glob
import shutil
import argparse


def replace_file_content(file_path: str, old_content: str, new_content: str) -> None:
    """
    Replace old_content with new_content in the specified file.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()

        if old_content in content:
            content = content.replace(old_content, new_content)

        with open(file_path, "w") as file:
            file.write(content)

        print(f"Updated {file_path}")

    except Exception as e:
        print(f"Error updating {file_path}: {e}")


def copy_fuzz_utils(time_budget: int = 180):
    """
    Copy coverage fuzzing utilities to every PyTorch API directory.
    Supports both:
        torch.xxx
    and:
        torch_cpu/torch.xxx
    directory layouts.
    """

    fuzz_sh = "fuzz.sh"
    build_sh = "build.sh"
    random_seed = "random_seed.py"
    coverage_py = "coverage_fuzzing.py"
    fuzzer_utils_h = "fuzzer_utils.h"
    fuzzer_utils_cpp = "fuzzer_utils.cpp"


    # Find all PyTorch API directories
    torch_dirs = [
        d for d in glob.glob("torch.*")
        if os.path.isdir(d)
    ]

    if not torch_dirs:
        print("No PyTorch API directories found!")
        return False

    print(f"Found {len(torch_dirs)} PyTorch API directories")


    # Copy files into each API directory
    for torch_dir in torch_dirs:

        api_name = os.path.basename(torch_dir)

        print(
            f"Processing directory: {torch_dir} "
            f"(API: {api_name})"
        )


        target_fuzz_sh = os.path.join(
            torch_dir,
            "fuzz.sh"
        )

        target_build_sh = os.path.join(
            torch_dir,
            "build.sh"
        )

        target_random_seed = os.path.join(
            torch_dir,
            "random_seed.py"
        )

        target_coverage_py = os.path.join(
            torch_dir,
            "coverage_fuzzing.py"
        )

        target_fuzzer_utils_h = os.path.join(
            torch_dir,
            "fuzzer_utils.h"
        )

        target_fuzzer_utils_cpp = os.path.join(
            torch_dir,
            "fuzzer_utils.cpp"
        )


        try:

            shutil.copy2(
                fuzz_sh,
                target_fuzz_sh
            )

            shutil.copy2(
                build_sh,
                target_build_sh
            )

            shutil.copy2(
                random_seed,
                target_random_seed
            )

            shutil.copy2(
                coverage_py,
                target_coverage_py
            )

            shutil.copy2(
                fuzzer_utils_h,
                target_fuzzer_utils_h
            )

            shutil.copy2(
                fuzzer_utils_cpp,
                target_fuzzer_utils_cpp
            )


            # Replace placeholders
            replace_file_content(
                target_fuzz_sh,
                "{api_name}",
                api_name
            )


            replace_file_content(
                target_build_sh,
                "{api_name}",
                api_name
            )


            replace_file_content(
                target_fuzz_sh,
                "{time_budget}",
                str(time_budget)
            )


            print(
                f"Copied coverage utils to {torch_dir}"
            )


        except Exception as e:

            print(
                f"Error copying to {torch_dir}: {e}"
            )


    return True



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=
        "Copy coverage fuzzing utilities to PyTorch API directories."
    )


    parser.add_argument(
        "--time_budget",
        type=int,
        default=180,
        help=
        "Time budget in seconds for fuzzing."
    )


    args = parser.parse_args()


    print(
        "Copying PyTorch coverage fuzzing utilities..."
    )


    success = copy_fuzz_utils(
        args.time_budget
    )


    if success:
        print("Done!")
    else:
        print("Operation failed!")
