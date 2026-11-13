# 47. Permutations II

## Problem

Given an array of integers that may contain duplicates, return all possible unique permutations.

## Approach

The solution uses sorted backtracking:

1. Sort `nums` so equal values are adjacent.
2. Track the current permutation in `path` and used indices in `used`.
3. Skip an index that has already been used in the current permutation.
4. Skip a duplicate value when the identical value immediately before it has not been selected in the current path.
5. Add each completed permutation to `result`.

The duplicate check requires equal values to be selected in index order within a path. This prevents duplicate branches while still allowing repeated values to appear in the same permutation.

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

## Why `used[i - 1]` matters

For the sorted input `[1, 1, 2]`, the equal `1` values are at indices `0` and `1`.

- With `path = []`, index `0` is available. Index `1` is skipped because
  `used[0]` is false: starting with the second `1` would repeat the same branch.
- After choosing index `0`, `path = [1]` and `used[0]` is true. Index `1` is
  now allowed, so the method can build `[1, 1, 2]` using both input elements.

The check gives equal values a consistent index order within each path.
It prevents duplicate branches while allowing the input's repeated values
to appear together in a permutation.

## Complexity

Let `n` be the number of input values and `M` be the number of unique permutations:

- **Time:** `O(n log n + n * n!)` in the worst case, including sorting, backtracking checks, and copying results.
- **Space:** `O(n * M)` for the returned permutations, plus `O(n)` for the recursion path and `used` array.

## Python Implementation

See [47-Permutation-II.py](./47-Permutation-II.py).

## Reference

- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
