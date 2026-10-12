# 476. Number Complement

This folder contains the Python solution for LeetCode problem 476: Number Complement.

## Problem summary
Given a positive integer `num`, return the complement number. The complement of a number is the number obtained by flipping all bits in its binary representation.

Example:
- Input: `5` (`101` in binary)
- Output: `2` (`010` in binary)

## Solution approach
The solution uses a bitmask to flip every bit in the number:

1. Compute the number of bits in `num` using `num.bit_length()`.
2. Create a mask of the same length with all bits set to `1`:
   - `mask = (1 << bits) - 1`
3. XOR the original number with the mask:
   - `num ^ mask`

Because XOR with `1` flips a bit, XORing with a mask of all `1`s flips every bit in the range of the number.

## Code
See [476-Number Complement.py](./476-Number%20Complement.py).

## Complexity
- Time: `O(1)` (bit operations on a fixed-size integer)
- Space: `O(1)`
