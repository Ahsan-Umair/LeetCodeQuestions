# Remove Element

## Problem

Given an integer array `nums` and an integer `val`, remove every occurrence of
`val` in-place. Return `k`, the number of elements that remain after removal.
The first `k` positions of `nums` must contain the remaining elements; values
after position `k - 1` do not matter.

## Approach

The solution uses a write pointer, `k`, to track the next position where a
value different from `val` should be stored. It scans the array once:

1. If the current value is not `val`, copy it to `nums[k]`.
2. Increment `k` after storing a retained value.
3. Return `k` as the new logical length of the array.

Because values are written back into the original list, the array is modified
in-place without allocating another array.

## Complexity

- **Time:** `O(n)`, where `n` is the length of `nums`
- **Space:** `O(1)` auxiliary space

## Implementation

The implementation is in
[`27-Remove-Elements.py`](./27-Remove-Elements.py).
