# 461. Hamming Distance

## Problem

Given two non-negative integers `x` and `y`, return the Hamming distance between them. The Hamming distance is the number of bit positions where their binary representations differ.

## Approach

1. Convert `x` and `y` to binary strings.
2. Pad the shorter string with leading zeroes so both strings have the same length.
3. Compare corresponding bits and count the positions that differ.

For example, `x = 1` (`001`) and `y = 4` (`100`) differ in all three positions, so the distance is `3`.

## Complexity

- **Time:** `O(log(max(x, y)))`
- **Space:** `O(log(max(x, y)))`

The logarithm represents the number of bits needed to represent the larger integer.