# 46. Permutations

## Problem

Given an array of distinct integers `nums`, return every possible permutation of the array.

## Approach

The solution uses backtracking to build one permutation at a time:

1. Keep the current partial permutation in `path`.
2. Try each number that is not already in `path`.
3. Add the number, recurse, and then remove it to restore the previous state.
4. When `path` contains every input number, append a copy to `result`.

Copying the completed path is necessary because `path` is reused during backtracking.

## Example

```text
Input:  nums = [1, 2, 3]

Output:
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
```

## Small backtracking walkthrough

For `nums = [1, 2]`, the first branch builds `[1]`, then `[1, 2]`.
The completed path is copied into `result`. Returning from the recursive
calls removes `2` and then `1`, restoring `path` to `[]`.

The next branch starts with `2` and builds `[2, 1]`. After that result is
saved and the choices are undone, the method returns `[[1, 2], [2, 1]]`.
At each level, `num in path` prevents choosing a value already in that
permutation. This works because the problem guarantees distinct input values.

## Complexity

For `n` input values:

- **Time:** `O(n^2 * n!)`, including the linear membership check and copying each permutation.
- **Space:** `O(n * n!)` for the returned permutations, plus `O(n)` recursion and path space.

## Python Implementation

See [46-Permutations.py](./46-Permutations.py).

## Reference

- [46. Permutations](https://leetcode.com/problems/permutations/)
