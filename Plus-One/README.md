# 66. Plus One

## Problem

Treat an array of decimal digits as a nonnegative integer, add one, and return the resulting digits.

## Approach

The solution scans from right to left. A digit below nine is incremented and returned immediately; a nine becomes zero and carries to the next position. If the leading digit also carries, a new `1` is inserted at the front.

## Carry walkthrough

For `digits = [1, 9, 9]`, the scan starts at the final digit:

| Index | Change | Digits afterward |
|---|---|---|
| `2` | `9 + 1` carries, leaving `0` | `[1, 9, 0]` |
| `1` | The next `9` also becomes `0` | `[1, 0, 0]` |
| `0` | `1` becomes `2`, ending the carry | `[2, 0, 0]` |

When the carry reaches a digit below nine, the method returns immediately:
earlier digits do not need to change.

## Boundary cases and mutation

- `[1, 2, 3]` returns `[1, 2, 4]` after changing only the last digit.
- `[9, 9]` returns `[1, 0, 0]`; every digit carries, so a leading `1` is inserted.
- `[0]` returns `[1]`.

The method changes the supplied `digits` list and returns that same list,
including when a new leading digit is inserted.

## Complexity

- Time: `O(n)`
- Space: `O(1) auxiliary space, excluding possible growth of the output array`

## Solution

- [Plus-One.py](./Plus-One.py)
