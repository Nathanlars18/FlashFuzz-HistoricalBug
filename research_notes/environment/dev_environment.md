# Development Environment

## Date

2026-07-29


# Hardware

GPU:

NVIDIA GeForce RTX 4060 Laptop GPU


# Operating System

WSL2

Ubuntu 22.04.5 LTS


# Python

Python:

3.10.12


# CUDA

CUDA Toolkit:

11.8


Driver:

561.xx


# cuDNN

Version:

8.9.7


# PyTorch

Version:

PyTorch 2.2.0a0+git8ac9b20


Source:

~/pytorch


Build:

Source build


# Build configuration

CUDA:

Enabled


cuDNN:

Enabled


TORCH_CUDA_ARCH_LIST:

8.9
## FlashFuzz PyTorch 2.2复现实验环境

日期：
2026-07-30


### 系统环境

OS:
Ubuntu 22.04.5 LTS

运行环境:
WSL2

Kernel:
6.18.33.2-microsoft-standard-WSL2


### 硬件环境

CPU:
12 cores

Memory:
11GB RAM

Swap:
8GB


### Docker环境

Docker Desktop:

Version 29.6.2


Docker Server:

正常运行。


### FlashFuzz环境

项目：

FlashFuzz


目标：

复现FlashFuzz论文中的深度学习API fuzz测试流程。


### CUDA环境

Base image:

nvidia/cuda:11.8.0-devel-ubuntu22.04


### PyTorch环境

版本：

PyTorch v2.2.0


成功构建镜像：

ncsuswat/flashfuzz:torch2.2-base


镜像包含：

- CUDA 11.8
- clang/llvm
- PyTorch源码
- FlashFuzz编译依赖

MAX_JOBS:

2


# Verification


torch.cuda.is_available()

Result:

True


GPU:

RTX 4060 Laptop GPU


CUDA:

11.8


cuDNN:

8907



# Problems solved


## 1. CUDA compilation killed


Problem:

CUDA compilation process was killed.


Reason:

Too much memory usage during parallel compilation.


Solution:

Set:

MAX_JOBS=2



## 2. NumPy ABI conflict


Problem:

PyTorch compilation failed because NumPy 2.x was incompatible.


Solution:

Install:

numpy==1.26.4



## 3. cuDNN missing


Problem:

libcudnn not found.


Solution:

Install:

libcudnn8
libcudnn8-dev



# FlashFuzz Environment

Repository:

~/FlashFuzz


Target Framework:

PyTorch


Fuzzing Framework:

LLVM libFuzzer


Compiler:

clang++


Harness Generation:

LLM-based C++ harness generation


Current Status:

PyTorch environment prepared.

FlashFuzz runtime environment is not fully configured yet.


Pending Components:

- Docker installation
- FlashFuzz container setup
- Single API fuzzing verification
## 2026-08-03 FlashFuzz PyTorch环境搭建

### Docker环境

完成Docker Desktop配置。

验证：

- Docker version: 29.6.2
- Docker Server: Docker Desktop
- WSL2 Ubuntu 22.04

### FlashFuzz环境

成功构建：

ncsuswat/flashfuzz:torch2.2-base

包含：

- CUDA 11.8
- clang 14
- cmake 3.22
- PyTorch v2.2.0源码


### PyTorch fuzz编译

进入容器：

flashfuzz-torch22


创建：

/root/pytorch/build-fuzz


使用clang完成PyTorch fuzz版本编译：

make -j2


结果：

[100%] Built target torch_python
[100%] Built target nnapi_backend
[100%] Built target functorch


状态：

PyTorch fuzz backend配置完成。
## Docker Experiment Images

Created Docker checkpoints:

### flashfuzz-torch22-base-ready

Purpose:
Save environment after preparing FlashFuzz fuzz workspace.

### flashfuzz-torch22-pytorch-built

Purpose:
Save environment after compiling PyTorch with fuzz configuration.

### flashfuzz-torch22-verified

Purpose:
Final verified environment.

Contains:
- PyTorch build-fuzz
- FlashFuzz harness
- torch.add fuzz executable

Verification:

ldd torch.add/fuzz

Confirmed linked libraries:

libtorch.so
libtorch_cpu.so
libc10.so

FlashFuzz official execution entry (run.py) was successfully initialized after installing host-side Python dependency (tqdm).

## FlashFuzz official runner compatibility

To match the image naming convention used by expmanager.py:
