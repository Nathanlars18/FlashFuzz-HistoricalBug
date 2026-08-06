# Exp004 Full FlashFuzz Baseline (600s)

## Configuration

- Framework: PyTorch
- Version: 2.2
- Backend: CPU
- Mode: fuzz
- Time budget: 600s
- Parallel workers: 1 per API

## API

torch.add

## Result

rounds: 201886
invalid: 111832
valid: 90054
validity_ratio: 0.446064

