# 836. Rectangle Overlap

## Problem

Determine whether two axis-aligned rectangles overlap with positive area.

## Approach

The rectangles do not overlap if one is completely to the left, right, above, or below the other. The solution checks those four separating conditions and returns true only when none applies.

## Complexity

- Time: `O(1)`
- Space: `O(1)`

## Solution

- [836-Rectangle-Overlap.py](./836-Rectangle-Overlap.py)
