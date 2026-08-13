#!/bin/bash

set -e

rm -rf coverage_data

python3 coverage_fuzzing.py \
    --api torch.matmul \
    --interval 60 \
    --max-time 300 \
    --coverage-dir coverage_data
