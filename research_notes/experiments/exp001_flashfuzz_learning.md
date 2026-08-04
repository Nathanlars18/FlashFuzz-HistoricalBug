# Experiment 001

Title:

Understanding FlashFuzz Architecture and Preparing Reproduction


Date:

2026-07-29


## Goal

Understand FlashFuzz source code and prepare environment for reproduction.


## Repository

Location:

~/FlashFuzz


GitHub:

https://github.com/ncsu-swat/FlashFuzz



# Completed Work


## 1. FlashFuzz Pipeline Understanding


The overall workflow:


API list

↓

run.py

↓

Experiment Manager

↓

LLM harness generation

↓

C++ harness

↓

Compilation

↓

LLVM libFuzzer executable

↓

Fuzzing


---

## 2. run.py


Responsibilities:

- Parse experiment arguments
- Select framework and version
- Load API list
- Create Experiment objects


Understanding:

run.py is the experiment entry point.


---

## 3. expmanager.py


Responsibilities:

Experiment:

- Manage one API fuzz task
- Start container
- Execute commands
- Collect results


Scheduler:

- Manage multiple experiments
- Support parallel execution


Understanding:

One Experiment corresponds to one API.



---

## 4. Harness Generation


Location:

testharness_generation/torch_cpu


Main file:

llm_gptoss.py


Understanding:

LLM constructs prompts containing API information
and generates C++ fuzz harness code.


Output:

main.cpp



---

## 5. Harness Compilation


File:

scripts/build_test_harness.py


Process:


main.cpp

+

fuzzer_utils.cpp

+

libtorch


↓

clang++ -fsanitize=fuzzer


↓

fuzz executable



Understanding:

The harness is C++ source code.

Compilation links it with libFuzzer runtime
to create an executable fuzz target.



---

## 6. Fuzzing


File:

fuzz.sh


Process:


libFuzzer generates byte inputs

↓

LLVMFuzzerTestOneInput()

↓

decode bytes into tensors

↓

execute PyTorch API

↓

observe crashes or coverage



---

# Environment Status


Completed:

[x] WSL2 Ubuntu

[x] CUDA 11.8

[x] cuDNN 8.9.7

[x] PyTorch source build


Pending:

[ ] Docker setup

[ ] FlashFuzz complete execution


---

# Current Experiment Plan


Framework:

PyTorch


Testing Strategy:

Single API fuzzing first.


Parallelization:

Multiple independent APIs can be executed in parallel.


---

# Next Steps


1. Install Docker

2. Configure FlashFuzz runtime environment

3. Run one PyTorch API fuzzing experiment

4. Verify generated harness and fuzz execution

# Exp001 FlashFuzz复现实验记录


## Day 1 环境搭建与源码分析

日期：

2026-07-30


## 今日目标

完成FlashFuzz复现实验环境配置。


---

## 完成内容


### 1. Docker环境配置

安装Docker Desktop，并连接WSL2。

验证：

```bash
docker info
# Experiment 001 FlashFuzz reproduction

## Phase 1: Environment setup

Date:
2026-08-03

Goal:

复现FlashFuzz论文中的PyTorch fuzz环境。


## Completed

1. Git clone FlashFuzz
2. 配置Docker环境
3. 构建torch2.2-base镜像
4. 创建实验容器
5. 编译PyTorch fuzz版本


## Problems encountered

### Problem 1: Docker build timeout

原因：

Docker拉取nvidia/cuda镜像时网络超时。

解决：

手动docker pull后重新build。


### Problem 2: PyTorch clone失败

原因：

Git传输中断。

解决：

使用：

git config --global http.version HTTP/1.1

并降低clone深度。


### Problem 3: build_test_harness提前运行失败

原因：

没有生成：

/root/pytorch/build-fuzz

解决：

先完成PyTorch fuzz编译。


## Current status

Environment ready.

Next step:

1. 编译单API harness(torch.add)
2. 运行libFuzzer验证
3. 使用FlashFuzz run.py进行baseline实验
## 2026-08-03 torch.add End-to-End Validation

Objective:
Verify FlashFuzz PyTorch fuzzing pipeline.

Steps:

1. Start Docker environment.
2. Compile torch.add harness.
3. Verify binary linking.
4. Execute fuzz target.

Result:

Successfully executed torch.add fuzz target.

Observed:
- Random tensor generation
- Different dtype exploration
- Boundary tensor cases

Conclusion:

FlashFuzz PyTorch fuzz pipeline is functional.
Environment is ready for baseline experiments.O

## FlashFuzz official runner preparation

The original Docker build of torch2.2-fuzz was interrupted during mass harness compilation.

Instead, a verified Docker checkpoint was created after successful PyTorch fuzz build and torch.add validation.

The image was tagged as:

ncsuswat/flashfuzz:torch2.2-fuzz

to match FlashFuzz expmanager.py image naming convention.
