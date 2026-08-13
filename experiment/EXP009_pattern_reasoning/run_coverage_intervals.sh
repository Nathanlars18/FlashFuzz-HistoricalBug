#!/bin/bash

intervals=(
"60-120"
"120-180"
"180-240"
"240-300"
"300-360"
"360-420"
"420-480"
"480-540"
"540-600"
)

for interval in "${intervals[@]}"
do
    echo "Running coverage interval $interval"

    mkdir -p results/coverage_data/$interval

    LLVM_PROFILE_FILE="results/coverage_data/$interval/torch.matmul.profraw" \
    ./fuzz corpus \
    -max_total_time=60 \
    -print_final_stats=1

done
