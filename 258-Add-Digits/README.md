# 258. Add Digits

This solution addresses the LeetCode problem: Add Digits.

## Problem
Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit.

Example:
- Input: `38`
- Process: `3 + 8 = 11`, `1 + 1 = 2`
- Output: `2`

## Approach
The implementation keeps summing the digits of `num` until it becomes a single digit.

It does this by:
1. Repeatedly splitting the number into its digits using modulo and division.
2. Summing those digits.
3. Replacing the original number with the computed sum.
4. Stopping once the value is less than 10.

This works because the process is the standard repeated digit-sum method, which eventually reduces any number to its digital root.

## Time Complexity
- Each pass reduces the number of digits, so the total work is efficient.
- Time complexity: `O(log10(num))`
- Space complexity: `O(1)`

## Implementation
The solution is implemented in [258-Add-Digits.py](258-Add-Digits.py).
