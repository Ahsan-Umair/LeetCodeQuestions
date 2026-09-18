# 191. Number of 1 Bits — Binary String

## Problem

Count how many set bits (`1` bits) appear in the binary representation of a positive integer.

## Approach

The integer is converted to a binary string with `bin`. The solution then scans that string and increments a counter whenever the current character is `1`.

## Complexity

- Time: `O(log n)`
- Space: `O(log n) for the binary string`

## Solution

- [191-Number-of-One-Bits #1.py](./191-Number-of-One-Bits%20%231.py)
