# Project Context

## Project
Research on improving deep learning framework fuzzing with historical bug patterns.

## Current baseline
FlashFuzz reproduction.

Environment:
- Ubuntu 22.04 WSL2
- PyTorch 2.2.0 source build
- CUDA 11.8
- Docker based experiments

## Current completed work

1. Reproduced FlashFuzz torch2.2 CPU fuzzing.
2. Built 10 PyTorch API harnesses:
- torch.add
- torch.mul
- torch.matmul
- torch.mm
- torch.addmm
- torch.relu
- torch.sigmoid
- torch.softmax
- torch.tanh
- torch.exp

3. Completed baseline fuzz experiments.

## Current research direction

Use historical PyTorch bug patterns to enhance harness generation.

Future work:
- collect historical bug patterns
- map bug triggers to harness constraints
- compare baseline FlashFuzz vs enhanced harness

## Important files

run.py:
experiment entry.

expmanager.py:
experiment management.

scripts/build_test_harness.py:
harness generation/build.

scripts/template:
harness templates.