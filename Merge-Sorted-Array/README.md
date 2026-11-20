# 88. Merge Sorted Array

## Problem

Merge two sorted arrays into `nums1`, which has enough trailing space to hold all values.

## Approach

Three pointers work from right to left: one at each array's last valid element and one at the final write position. The larger remaining value is written first, preventing unread values in `nums1` from being overwritten.

## Valid values and spare capacity

Only the first `m` entries of `nums1` contain its input values. Its final
`n` slots are spare capacity for the merge. A zero inside the first `m`
entries is still a valid value; the pointers use the counts rather than the
values to decide which entries belong to the input.

## Worked example

For `nums1 = [1, 2, 3, 0, 0, 0]`, `m = 3`, `nums2 = [2, 5, 6]`, and `n = 3`:

| Write index | Value written | Source |
|---|---|---|
| `5` | `6` | `nums2` |
| `4` | `5` | `nums2` |
| `3` | `3` | `nums1` |
| `2` | `2` | `nums1`, chosen when the values are equal |
| `1` | `2` | `nums2` |

The remaining `1` is already at index `0`. The final `nums1` is
`[1, 2, 2, 3, 5, 6]`.

If `nums2` runs out first, the remaining prefix of `nums1` is already in
place. If `nums1` runs out first, the final loop copies the remaining values
from `nums2`. The method modifies `nums1` and returns `None`.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Solution

- [Merge-Sorted-Array.py](./Merge-Sorted-Array.py)
