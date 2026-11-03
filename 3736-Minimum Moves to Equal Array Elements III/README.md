# 3736. Minimum Moves to Equal Array Elements III

## Problem

Given an integer array `nums`, make every element equal using the fewest moves. In one move, an element can be increased by `1`.

## Approach

The final value must be at least the largest value already in the array because elements can only be increased. Choosing any value larger than the maximum would add unnecessary moves, so the optimal target is `max(nums)`.

For each element, the number of moves needed is `max(nums) - num`. Summing these differences gives the minimum total number of moves.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [3736-Minimum Moves to Equal Array Elements III.py](./3736-Minimum%20Moves%20to%20Equal%20Array%20Elements%20III.py)
