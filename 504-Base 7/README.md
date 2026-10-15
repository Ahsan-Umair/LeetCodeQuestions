# 504. Base 7

## Problem

Given an integer `num`, return its representation in base 7 as a string.

The result must preserve the sign for negative numbers, and zero should be
returned as `"0"`.

## Solution

The [`504-Base 7.py`](./504-Base%207.py) solution uses the standard base
conversion algorithm:

1. Return `"0"` immediately when the input is zero.
2. Record whether the input is negative and work with its absolute value.
3. Repeatedly divide the number by 7.
   - The remainder is the next base-7 digit.
   - Prepend each remainder to the result string.
4. Add `"-"` back when the original input was negative.

For example, `100` produces remainders `2`, `0`, and `2` from right to left,
so its base-7 representation is `"202"`.

## Complexity

- **Time:** `O(log_7 |num|)`
- **Space:** `O(log_7 |num|)` for the result string

## Usage

The file follows LeetCode's `Solution` class format:

```python
solution = Solution()
solution.convertToBase7(100)   # "202"
solution.convertToBase7(-7)    # "-10"
solution.convertToBase7(0)     # "0"
```
