# 9. Palindrome Number

## Problem

Determine whether an integer reads the same forward and backward.

## Approach

Negative values are rejected. For a nonnegative value, the solution reconstructs the reversed integer one decimal digit at a time and compares it with the original.

## Complexity

- Time: `O(log₁₀ n)`
- Space: `O(1)`

## Solution

- [Palindrome.py](./Palindrome.py)
