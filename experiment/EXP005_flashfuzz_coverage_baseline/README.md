# EXP005: FlashFuzz PyTorch Coverage Baseline

## 1. Experiment Goal

本实验目标是复现 FlashFuzz 在 PyTorch CPU API 上的 coverage fuzzing 流程，
建立后续 Historical Bug Pattern Enhanced Harness 实验的 baseline。


## 2. Experimental Environment

- OS: WSL2 Ubuntu
- Framework: PyTorch 2.2
- Device: CPU
- Compiler: clang
- Fuzzer: libFuzzer
- Framework: FlashFuzz


## 3. Experiment Motivation

后续研究目标：

Historical Bug Pattern Enhanced Harness

需要首先获得：

FlashFuzz original harness generation

情况下的测试效果。


因此本实验统计：

- fuzz execution
- branch coverage
- covered branches
- coverage trend


## 4. Implementation Problems and Solutions


### Problem 1: coverage_data not found


现象：

运行 coverage mode:
python3 run.py --dll torch --version 2.2 --mode cov


出现：

Could not find:
/root/fuzz/torch.matmul/coverage_data


原因：

PyTorch CPU harness实际路径：

/root/fuzz/torch_cpu/torch.xxx


但是脚本搜索：

torch.xxx


导致coverage结果无法复制。


解决：

修改：

scripts/template/torch_cpu_cov/copy.py


增加：

torch_cpu/torch.*

目录搜索。


---

### Problem 2: profraw files not collected


现象：

No profraw files found


原因：

expmanager.py复制路径错误。


解决：

修改：

expmanager.py


修复：

coverage_data结果复制逻辑。


---

### Problem 3: Docker command output unavailable


现象：

Docker内部错误无法定位。


原因：

execute_command:

subprocess.run()

没有输出stdout/stderr。


解决：

增加：

- capture_output
- stdout打印
- stderr打印


---

## 5. Verification


测试API:

torch.matmul


运行:

coverage_fuzzing.py


成功生成：

coverage_data/0-60/torch.matmul.profraw


最终运行:

run.py


成功完成：

- fuzz execution
- profraw collection
- profraw merge
- coverage extraction


结果：


Covered branches:

484


Total branches:

30094


Branch coverage:

1.61%


## 6. Code Version


Branch:

experiment/coverage-baseline


Commits:

789d9af
fix torch coverage harness generation and collect profraw correctly
eba1e89
fix coverage result collection in expmanager


## 7. Next Step


Run coverage baseline on 10 selected APIs:


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
# EXP005 FlashFuzz Coverage Baseline

## Goal

Evaluate FlashFuzz generated harness coverage performance on PyTorch 2.2 CPU APIs.

This experiment provides baseline data for later comparison with historical Bug Pattern enhanced harness generation.


## Environment

- Framework: PyTorch 2.2
- Platform: WSL2 Ubuntu
- Mode: coverage fuzzing
- Compiler: clang
- Backend: CPU


## Problems and Solutions


### Problem 1: Coverage container failed to collect profraw files

Symptom:

Coverage experiment completed but no coverage_data generated.


Cause:

The coverage harness generation and result collection scripts were not correctly handling profraw output.


Solution:

Modified:

- docker/torch-2.2-cov.Dockerfile
- scripts/template/torch_cpu_cov/copy.py

to correctly generate and copy profraw files.


Commit:

xxxxx


---


### Problem 2: Coverage result collection failure

Symptom:

Experiment finished but coverage summary could not be generated.


Cause:

expmanager.py did not correctly copy coverage files between containers.


Solution:

Modified expmanager.py to improve coverage result collection.

Commit:

eba1e89


---

## API Results

|API|Time|Coverage|
|-|-|-|
|torch.add|600s|235 branches|

# EXP005 FlashFuzz Coverage Baseline


## 1. Experiment Goal

This experiment evaluates the coverage performance of FlashFuzz generated harnesses on PyTorch CPU APIs.

The purpose of this experiment is to establish a baseline for later comparison with historical Bug Pattern enhanced harness generation.


## 2. Environment

- Framework: PyTorch 2.2
- Backend: CPU
- Platform: WSL2 Ubuntu
- Compiler: clang 14
- Fuzzing engine: libFuzzer
- Coverage mode: LLVM source coverage


## 3. Experimental Configuration

- Mode: coverage fuzzing
- Time budget: 600 seconds per API
- Target APIs:

torch.add
torch.mul
torch.matmul
torch.mm
torch.addmm
torch.relu
torch.sigmoid
torch.softmax
torch.tanh
torch.exp


## 4. Implementation Issues and Solutions


### Issue 1: Torch coverage image and harness generation

#### Symptom

The coverage experiment could not correctly generate coverage data.

#### Cause

The PyTorch coverage Docker environment and harness generation scripts were not fully compatible.

#### Solution

Modified:

- docker/torch-2.2-cov.Dockerfile
- scripts/template/torch_cpu_cov/copy.py

to correctly build the coverage environment and collect generated coverage files.


Commit:

789d9af7


---


### Issue 2: Coverage result collection failure

#### Symptom

The fuzzing process finished, but coverage results were not correctly copied from Docker containers.

#### Cause

The result collection logic in expmanager.py did not correctly handle coverage output.

#### Solution

Modified expmanager.py to improve coverage result collection and debugging information.

Commit:

eba1e89d


---


## 5. Results


### torch.add


Configuration:

- Time budget: 600s


Coverage result:

| Metric | Value |
|----|----|
| Covered branches | 235 |
| Total branches | 30094 |
| Branch coverage | 0.78% |


Coverage evolution:

| Time | Covered branches |
|-|-|
|0-60s|202|
|60-120s|202|
|120-180s|203|
|180-240s|203|
|240-300s|233|
|300-360s|233|
|360-420s|233|
|420-480s|235|
|480-540s|235|
|540-600s|235|


Result:

Successfully completed.
