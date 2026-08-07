# Historical Bug Pattern Schema


## 1. Metadata

- Pattern ID
- API Name
- Source
- Date
- Severity


## 2. Bug Category

Primary Category:

Secondary Category:


Available categories:

1 Shape Boundary
2 Dtype Boundary
3 Device Transition
4 Memory Layout
5 Numerical Edge Case
6 Gradient/Autograd
7 Backend Dispatch
8 Concurrency


## 3. Trigger Condition

- Shape Trigger
- Dtype Trigger
- Device Trigger
- Memory Trigger
- Value Trigger
- State Trigger
- Execution Trigger

Concrete Constraints:


## 4. Root Cause

- API Layer
- ATen Layer
- Kernel Layer
- Backend Layer
- Numerical Layer

Confidence:


## 5. Bug Oracle

- Crash
- Exception
- Incorrect Output
- Timeout/Hang
- Memory Error
The observable behavior used to determine whether a bug is triggered.

Types:

- Crash:
  Process termination, SIGSEGV, SIGBUS, SIGABRT.

- Exception:
  RuntimeError, ValueError, AssertionError.

- Wrong Result:
  Output differs from reference result.

- Hang:
  Operation exceeds execution time limit.

- Memory Corruption:
  Memory outside valid tensor region is modified.

## 6. Harness Strategy

- Input Mutation
- Tensor Construction
- Constraint Injection
- Operation Sequence

- Oracle Construction
## 7. Verification Status

Describe the confidence level of the historical bug information.


Fields:

- level:
  - fixed
  - official_triaged
  - user_reported

- fixed:
  - true
  - false


Example:

```json
{
  "verification_status": {
    "level": "official_triaged",
    "fixed": false
  }
}
```
