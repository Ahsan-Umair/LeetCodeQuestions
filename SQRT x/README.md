# 69. Sqrt(x)

## Problem

Return the integer square root of a nonnegative integer—the floor of its exact square root.

## Approach

Binary search examines candidate roots between zero and `x`. An exact square is returned immediately; otherwise, the search narrows according to whether `mid²` is too large or too small, and the final upper bound is the floor.

## Complexity

- Time: `O(log x)`
- Space: `O(1)`

## Solution

- [SQRT x.py](./SQRT%20x.py)
