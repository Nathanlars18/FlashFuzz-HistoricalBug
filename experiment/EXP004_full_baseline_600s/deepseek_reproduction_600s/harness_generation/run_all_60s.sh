#!/bin/bash

APIS=(
torch.add
torch.addmm
torch.exp
torch.matmul
torch.mm
torch.mul
torch.relu
torch.sigmoid
torch.softmax
torch.tanh
)

for api in "${APIS[@]}"
do

echo "====================="
echo $api
echo "====================="

cd /workspace/harness/$api

mkdir -p artifacts

./fuzz ./corpus \
-max_total_time=60 \
-print_final_stats=1 \
-artifact_prefix="./artifacts/" \
> fuzz_result.txt 2>&1

done
