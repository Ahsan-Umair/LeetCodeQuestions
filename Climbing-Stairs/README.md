# 70. Climbing Stairs

## Problem

Count the distinct ways to reach the top of a staircase when each move climbs one or two steps.

## Approach

The number of ways to reach a step is the sum of the previous two counts. The solution iteratively maintains only those two values instead of storing the full dynamic-programming table.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Climbing-Stairs.py](./Climbing-Stairs.py)
