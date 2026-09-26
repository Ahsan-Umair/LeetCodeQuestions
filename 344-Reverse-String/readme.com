# 344. Reverse String

## Problem

Reverse the input list of characters in place. The method must modify the original list and must not return a value.

## Approach

Use two pointers:

- `left` starts at the first character.
- `right` starts at the last character.
- Swap the characters at `left` and `right`.
- Move `left` forward and `right` backward.
- Continue until the pointers meet or cross.

This matches the implementation in `344-Reverse-String.py`.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

The list is reversed in place, so no additional list is needed.
