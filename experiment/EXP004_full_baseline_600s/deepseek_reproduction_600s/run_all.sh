#!/bin/bash

CONTAINER=flashfuzz-deepseek-exp004-600s

HOST_DIR=$HOME/FlashFuzz/experiment/EXP004_full_baseline_600s/deepseek_reproduction_600s/harness

CONTAINER_DIR=/workspace/harness


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

echo "================================="
echo "Running $api"
echo "================================="


docker exec $CONTAINER bash -c "
cd $CONTAINER_DIR/$api &&
bash build.sh &&
mkdir -p artifacts &&
./fuzz ./corpus \
-max_total_time=600 \
-print_final_stats=1 \
-artifact_prefix='./artifacts/' \
> fuzz_result.txt 2>&1
"


if [ $? -ne 0 ]; then
    echo "$api failed"
else
    echo "$api finished"
fi


done


echo "All APIs finished"
