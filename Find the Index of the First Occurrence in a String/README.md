# 28. Find the Index of the First Occurrence in a String

## Problem

Return the starting index of the first occurrence of `needle` in `haystack`, or `-1` if it is absent.

## Approach

Every feasible start position in the haystack is tried. An inner loop compares the needle character by character and stops immediately on a mismatch; the first complete match is returned.

## Complexity

- Time: `O((h - n + 1) × n) in the worst case`
- Space: `O(1)`

## Solution

- [Find the Index of the First Occurrence in a String.py](./Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String.py)
