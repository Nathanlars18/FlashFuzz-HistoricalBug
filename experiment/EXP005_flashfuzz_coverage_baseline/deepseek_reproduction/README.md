# EXP005 FlashFuzz Coverage Baseline

## Goal

Reproduce FlashFuzz baseline with DeepSeek-generated PyTorch harnesses.

## Environment

- PyTorch: 2.2.0a0
- CUDA: disabled
- CPU fuzzing
- LLVM coverage

## APIs

10 PyTorch APIs:

- torch.add
- torch.mul
- torch.matmul
- torch.mm
- torch.addmm
- torch.exp
- torch.relu
- torch.sigmoid
- torch.softmax
- torch.tanh


## Configuration

Fuzzing time:
600 seconds per API

Coverage interval:
60 seconds


## Metrics

Branch coverage collected by:

llvm-cov + llvm-profdata


## Results

See:

baseline_summary.txt
