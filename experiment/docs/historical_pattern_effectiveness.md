# Historical Bug Pattern Effectiveness Analysis


## 1. Background

Large Language Models (LLMs) have shown promising
capabilities in generating fuzzing harnesses for
deep learning frameworks.

However, existing LLM-based harness generation
approaches mainly rely on:

- API documentation
- Function signatures
- Existing code templates


These information can help LLMs generate valid
API calls, but they provide limited guidance about
where bugs are likely to appear.

Historical bug reports contain valuable information
about:

- triggering conditions
- root causes
- abnormal input characteristics

Therefore, this work investigates whether
historical bug knowledge can improve LLM-based
harness generation.

## 2. Historical Bug Pattern Definition


A historical bug pattern is an abstraction of
previous bug reports.

Instead of directly replaying a bug-triggering
input, we extract general testing knowledge,
including:

- affected API
- trigger condition
- input characteristics
- possible root cause
- testing strategy


The goal is to transform historical bugs into
reusable fuzzing guidance.

## 3. Why Historical Patterns Improve Harness Generation


Random fuzzing mainly explores the input space
without prior knowledge.

For deep learning frameworks, the input space is
high-dimensional, including:

- tensor shape
- dtype
- memory layout
- device
- gradient state


Historical bug patterns provide information about
bug-sensitive dimensions.


For example, in torch.matmul:

Without historical knowledge:

    random tensor generation


With historical knowledge:

    unaligned memory
    zero dimension
    non-contiguous tensor
    output storage boundary


Therefore, historical patterns guide the LLM to
generate more targeted input construction strategies.

## 4. Evaluation Metrics

To evaluate whether historical bug patterns improve
LLM-based harness generation, we consider four aspects:

1. Harness Generation Quality

2. Historical Bug Pattern Utilization

3. Fuzzing Effectiveness

4. Bug Discovery Capability
### 4.1 Harness Generation Quality

Historical bug patterns are expected to improve
the quality of generated harnesses.

We evaluate harness generation using:

- Compile Success Rate:
  Whether the generated harness can be successfully
  compiled.

- Execution Success Rate:
  Whether the compiled harness can successfully execute
  fuzzing campaigns.

These metrics measure whether historical knowledge
can be effectively integrated into LLM-generated
harnesses without reducing generation reliability.


### 4.2 Historical Bug Pattern Utilization

Since the core motivation of this work is using
historical bug knowledge to guide harness generation,
we evaluate whether the generated harness actually
implements the provided historical patterns.


The Pattern Utilization Rate is defined as:

Pattern Utilization Rate =
Implemented Historical Patterns /
Provided Historical Patterns


For example, in the torch.matmul multi-pattern
experiment, four historical patterns are provided:

- Unaligned Memory
- Zero Dimension Tensor
- Non-contiguous Tensor View
- Output Storage Boundary


The generated harness is analyzed to determine
whether these bug-triggering strategies are
successfully incorporated.


### 4.3 Fuzzing Effectiveness

To evaluate whether pattern-enhanced harnesses improve
testing capability, we measure:

- Branch Coverage:
  The amount of internal framework code paths explored.

- Coverage Growth:
  The increase of coverage over fuzzing time.

- Newly Added Units:
  The number of new inputs discovered by the fuzzer.

- Execution Throughput:
  The number of executions per second.


These metrics evaluate whether historical knowledge
helps the generated harness explore deeper behaviors
inside deep learning frameworks.


### 4.4 Bug Discovery Capability

The ultimate goal of fuzzing is discovering real
framework defects.

Therefore, we consider:

- Crash Number:
  Total crashes triggered during fuzzing.

- Unique Crash Number:
  Number of deduplicated crashes.

- Valid Bug Rate:
  The ratio of confirmed framework bugs among all
  detected crashes.


These metrics evaluate whether historical bug patterns
can improve the ability to discover real defects.

## 5. Experimental Evidence

The current evaluation focuses on validating whether
historical bug patterns can influence LLM-generated
harness construction.

Large-scale evaluation across multiple APIs is planned
as future work.

### 5.1 Single Pattern Guidance (EXP007)


EXP007 investigates whether one historical bug
pattern can influence LLM-generated harnesses.


Compared with baseline:

- The generated harness contains additional
  bug-oriented input strategies.
- The fuzzing process discovers more new units.


This demonstrates that historical knowledge can
modify LLM harness generation behavior.

### 5.2 Multi Pattern Guidance (EXP008)


EXP008 extends single pattern guidance by
providing multiple historical patterns.


The generated harness introduces:

| Pattern | Strategy |
|-|-|
|Unaligned Memory|Memory alignment testing|
|Zero Dimension|Boundary shape testing|
|Non-contiguous View|Tensor layout testing|
|Output Boundary|Output storage constraint testing|


Compared with the baseline harness:

- Newly discovered fuzzing units increased from 299 to 985.
- Final branch coverage increased from 1.68% to 1.89%.

This indicates that multiple historical patterns can provide
more targeted guidance for harness generation.

## 6. Current Limitations


Although historical patterns improve harness
generation, the current approach still relies on
manual pattern extraction and selection.


Current pipeline:

Bug Report

↓

Human Analysis

↓

Pattern Extraction

↓

Prompt Injection

↓

LLM Harness Generation


This limits scalability because:

1. Pattern extraction requires human effort.
2. Manual selection may not generalize to new APIs.
3. The LLM does not explicitly reason about
historical knowledge.


## 7. Future Direction


The next step is to build a historical bug
knowledge base and enable LLMs to reason about
historical patterns.


Instead of forcing the LLM to reproduce existing
patterns, historical knowledge should serve as
reference information.


The LLM should:

1. Understand bug characteristics.
2. Select relevant knowledge.
3. Generate appropriate testing strategies.
4. Create novel inputs beyond existing patterns.
