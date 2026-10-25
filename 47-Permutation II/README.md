# 47. Permutations II

## Problem

Given an array of integers that may contain duplicates, return all possible unique permutations.

## Approach

The solution uses sorted backtracking:

1. Sort `nums` so equal values are adjacent.
2. Track the current permutation in `path` and used indices in `used`.
3. Skip an index that has already been used in the current permutation.
4. Skip a duplicate value when the identical value immediately before it has not been used at the current recursion level.
5. Add each completed permutation to `result`.

The duplicate check allows the first copy of a value to be selected before another identical copy at the same depth, preventing duplicate branches while still allowing equal values to appear in different positions.

## Example

```text
Input:  nums = [1, 1, 2]

Output:
[
  [1, 1, 2],
  [1, 2, 1],
  [2, 1, 1]
]
```

## Complexity

Let `n` be the number of input values and `M` be the number of unique permutations:

- **Time:** `O(n log n + n * n!)` in the worst case, including sorting, backtracking checks, and copying results.
- **Space:** `O(n * M)` for the returned permutations, plus `O(n)` for the recursion path and `used` array.

## Python Implementation

See [47-Permutation-II.py](./47-Permutation-II.py).

## Reference

- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
