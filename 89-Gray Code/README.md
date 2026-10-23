# 89. Gray Code

## Problem

Given an integer `n`, return a sequence of `2^n` integers representing an `n`-bit Gray code. The sequence starts with `0`, and every pair of adjacent values differs by exactly one bit. The first and last values must also differ by one bit.

## Approach

The solution constructs the sequence iteratively using reflection:

1. Start with `[0]` for zero bits.
2. For each bit position `i`, iterate through the current sequence in reverse order.
3. Add `1 << i` to each reflected value and append it to the sequence.
4. Continue until all `n` bit positions have been processed.

Adding the new bit to the reflected half guarantees that each newly added value differs from its predecessor by one bit.

## Example

```text
n = 2

Start:       [0]
Add bit 0:   [0, 1]
Add bit 1:   [0, 1, 3, 2]

Output: [0, 1, 3, 2]
```

## Complexity

- **Time:** `O(2^n)`, because the sequence contains `2^n` values.
- **Space:** `O(2^n)` for the returned sequence.

## Python Implementation

See [89-Gray-Code.py](./89-Gray-Code.py).

## Reference

- [89. Gray Code](https://leetcode.com/problems/gray-code/)
