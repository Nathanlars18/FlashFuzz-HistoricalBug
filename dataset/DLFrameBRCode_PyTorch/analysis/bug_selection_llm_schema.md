# LLM Bug Selection Output Schema


## Purpose

Determine whether a historical PyTorch bug report
can be converted into reusable bug patterns and
knowledge for fuzzing harness generation.


## Output Fields


### bug_id

The original bug identifier.


### target_api

The main PyTorch API affected by the bug.


### bug_category

General bug pattern category.

Examples:

- Shape Boundary
- Memory Layout Boundary
- Dtype Boundary
- Device Boundary
- Gradient Boundary
- State Boundary


### trigger_condition

The input condition that triggers the bug.


Example:

Non-contiguous CUDA tensor with abnormal stride.


### oracle_type

Observable failure behavior.

Options:

- Crash
- Exception
- Incorrect Output
- Performance Issue
- Documentation Issue


### pattern_extractability

Whether the bug can be generalized.

Values:

- High
- Medium
- Low


### knowledge_generation_feasibility

Whether the bug can generate harness guidance.

Values:

- High
- Medium
- Low


### include

Whether the bug should be included.

Values:

- Yes
- No


### reason

Explain the decision.


### confidence

LLM confidence:

- High
- Medium
- Low
