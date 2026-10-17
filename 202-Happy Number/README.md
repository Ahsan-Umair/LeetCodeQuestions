# 202. Happy Number

## Problem

Determine whether a positive integer `n` is a happy number. A number is happy if repeatedly replacing it with the sum of the squares of its digits eventually produces `1`. If the process enters a cycle that does not include `1`, the number is not happy.

## Approach

The solution uses a set to track numbers that have already appeared:

1. Start with `n`.
2. Calculate the sum of the squares of its digits.
3. Continue until the current number is `1` or has already been seen.
4. Return `True` only when the process reaches `1`.

Tracking previously seen values prevents an infinite loop when the sequence enters a cycle.

## Example

```text
Input:  n = 19

19 -> 1^2 + 9^2 = 82
82 -> 8^2 + 2^2 = 68
68 -> 6^2 + 8^2 = 100
100 -> 1^2 + 0^2 + 0^2 = 1

Output: True
```

## Complexity

- **Time:** `O(k * log n)`, where `k` is the number of generated sequence values. For this problem, the sequence reaches `1` or a cycle after a bounded number of steps.
- **Space:** `O(k)` for the set of previously seen values.

## Python Implementation

See [202-Happy-Number.py](202-Happy-Number.py).

## Reference

- [202. Happy Number](https://leetcode.com/problems/happy-number/)
