# 344. Reverse String

## Problem

Reverse an array of characters in place without allocating another array.

## Approach

Use two pointers, one at each end of the array. Swap their characters, then move both pointers toward the center until they meet. The method modifies `s` directly and returns nothing.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [344-Reverse-String.py](./344-Reverse-String.py)
