# 67. Add Binary

## Problem

Add two binary strings and return their sum as another binary string.

## Approach

Two indices scan the inputs from right to left. At each position, the two digits and carry are added; modulo two produces the output digit and integer division produces the next carry. Digits are inserted at the front of the result list.

## Adding strings of different lengths

For `a = "111"` and `b = "1"`, the scan reads columns from right to left.
Once `b` runs out of digits, its digit is treated as `0`.

| Column | Digit from `a` | Digit from `b` | Carry in | Output digit | Carry out |
|---|---:|---:|---:|---:|---:|
| Rightmost | 1 | 1 | 0 | 0 | 1 |
| Next | 1 | 0 | 1 | 0 | 1 |
| Leftmost input digit | 1 | 0 | 1 | 0 | 1 |
| Final carry | 0 | 0 | 1 | 1 | 0 |

The `or carry` condition keeps the loop running after both inputs are
exhausted, so the final `1` is added to the front. The result is `"1000"`.

## Complexity

Let `L` be the length of the result.

- Time: `O(L²)` because each front insertion shifts the existing digits.
- Space: `O(L)` for the digit list and the returned string.

## Solution

- [Add-Binary.py](./Add-Binary.py)
