# 342. Power of Four

## Problem

Determine whether an integer is an exact power of four.

## Approach

While the value is positive and divisible by four, the solution divides it by four. It is a power of four only when this process finishes at exactly `1`.

## Complexity

- Time: `O(log₄ n)`
- Space: `O(1)`

## Solution

- [342-Power-of-Four.py](./342-Power-of-Four.py)
