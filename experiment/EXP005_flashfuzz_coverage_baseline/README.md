# EXP005 FlashFuzz Coverage Baseline


## Goal

Evaluate FlashFuzz generated harness coverage performance on PyTorch 2.2 CPU APIs.

This experiment establishes baseline results for later Historical Bug Pattern Enhanced Harness comparison.


## Environment

- OS: WSL2 Ubuntu
- Framework: PyTorch 2.2
- Backend: CPU
- Compiler: clang 14
- Fuzzer: libFuzzer
- Mode: LLVM coverage fuzzing


## Configuration

Target APIs:

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


Time budget:

600 seconds/API


## Problems and Solutions


### Problem 1: Coverage data collection failure

Symptom:

No profraw files found.

Cause:

Coverage harness output path mismatch.

Solution:

Modified:

- docker/torch-2.2-cov.Dockerfile
- scripts/template/torch_cpu_cov/copy.py


Commit:

789d9af7


### Problem 2: Coverage result collection failure

Symptom:

Coverage summary could not be generated.

Cause:

expmanager.py copied results incorrectly.

Solution:

Modified expmanager.py.

Commit:

eba1e89d


## Results


| API | Time | Covered branches |
|-|-|-|
|torch.add|600s|235|


Coverage trend:

|Time|Branches|
|-|-|
|0-60|202|
|60-120|202|
|120-180|203|
|180-240|203|
|240-300|233|
|300-360|233|
|360-420|233|
|420-480|235|
|480-540|235|
|540-600|235|


## Next Step

Run remaining APIs.
