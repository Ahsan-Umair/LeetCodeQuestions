# 1. Two Sum — Hash Map

## Problem

Return the indices of two distinct array elements whose sum equals the target.

## Approach

While scanning the array, the solution computes the complement needed for the current value. If that complement was seen earlier, its stored index and the current index form the answer; otherwise, the current value and index are stored.

## Complexity

- Time: `O(n) on average`
- Space: `O(n)`

## Solution

- [Two-Sum-Approach # 2.py](./Two-Sum-Approach%20%23%202.py)
