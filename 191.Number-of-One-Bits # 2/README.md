# 191. Number of 1 Bits — Bit Shifting

## Problem

Count how many set bits (`1` bits) appear in the binary representation of a positive integer.

## Approach

The solution repeatedly reads the least-significant bit with `n & 1`, adds it to the count when it is set, and shifts the number one position to the right until no bits remain.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Solution

- [191.Number-of-One-Bits # 2.py](./191.Number-of-One-Bits%20%23%202.py)
