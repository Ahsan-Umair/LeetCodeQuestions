# 338. Counting Bits

## Problem

Given an integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the number of `1` bits in the binary representation of `i`.

## Approach

For each number from `0` to `n`:

1. Inspect its least significant bit with `num & 1`.
2. Add that bit to the count.
3. Shift the number right by one position.
4. Repeat until the number becomes `0`.

Append each count to the result array.

## Example

```text
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]

Binary values:
0 -> 0       -> 0 bits
1 -> 1       -> 1 bit
2 -> 10      -> 1 bit
3 -> 11      -> 2 bits
4 -> 100     -> 1 bit
5 -> 101     -> 2 bits
```

## Complexity

- **Time:** `O(n log n)` in the worst case, since each number is processed one binary digit at a time.
- **Space:** `O(n)` for the returned array.

## Reference

- [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
