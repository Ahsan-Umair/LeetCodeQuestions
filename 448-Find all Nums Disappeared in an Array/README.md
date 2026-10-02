# 448. Find All Numbers Disappeared in an Array

## Problem

Given an integer array `nums` containing `n` numbers where each number is in the
range `[1, n]`, return all numbers in that range that do not appear in `nums`.

## Solution

The solution in
[`448-Find-all-nums-disappeared-in-an-array.py`](./448-Find-all-nums-disappeared-in-an-array.py)
stores every value from `nums` in a set. It then checks each number from `1` to
`n` and adds numbers that are not present in the set to the result.

### Why it works

The set provides a complete record of the values that occur in the input.
Therefore, checking every value in `[1, n]` identifies exactly the numbers that
are missing.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(n)` for the set and result list

## Usage

```python
from importlib.util import module_from_spec, spec_from_file_location

path = "448-Find-all-nums-disappeared-in-an-array.py"
spec = spec_from_file_location("solution", path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

solution = module.Solution()
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
# [5, 6]
```
