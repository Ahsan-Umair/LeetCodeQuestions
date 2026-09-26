# 136. Single Number

## Problem

Every array value appears twice except one. Return the value that appears once.

## Approach

All values are combined with bitwise XOR. Equal pairs cancel because `x XOR x = 0`, leaving only the unpaired value.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Single-Number.py](./Single-Number.py)
