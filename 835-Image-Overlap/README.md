# 835. Image Overlap

## Problem

Translate one square binary image over another and return the largest number of positions where both images contain `1`.

## Approach

The solution tries every row and column shift from `-(n - 1)` through `n - 1`. For each shift, it scans all cells, checks whether the translated coordinate stays in bounds, and counts overlapping `1` values.

## Complexity

- Time: `O(n⁴)`
- Space: `O(1)`

## Solution

- [835-Image-Overlap.py](./835-Image-Overlap.py)
