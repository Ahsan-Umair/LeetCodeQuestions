# 35. Search Insert Position

## Problem

In a sorted array, return the index of a target or the index where it should be inserted to preserve order.

## Approach

Binary search narrows the inclusive search range. If the target is absent, `left` finishes at the first position containing a larger value, which is exactly the insertion index.

## Worked example

For `nums = [1, 3, 5, 6]` and `target = 2`:

| `left` | `right` | `mid` | Value checked | Update |
|---|---|---|---|---|
| `0` | `3` | `1` | `3` | Set `right = 0` because `3 > 2` |
| `0` | `0` | `0` | `1` | Set `left = 1` because `1 < 2` |

Now `left > right`, so the loop ends and returns `1`. Inserting `2` at
index `1` preserves the sorted order: `[1, 2, 3, 5, 6]`.

## Boundary cases

For the same input array:

- Target `5` returns its existing index, `2`.
- Target `0` returns `0`, before every existing value.
- Target `7` returns `4`, after the last element. An insertion index can equal
  the length of the array.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Solution

- [Search-Insert-Position.py](./Search-Insert-Position.py)
