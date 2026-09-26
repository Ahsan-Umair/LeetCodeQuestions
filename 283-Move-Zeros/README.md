# 283. Move Zeroes

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note:** You must do this in-place without making a copy of the array.

### Examples

| Input | Output |
|---|---|
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` |
| `[0]` | `[0]` |

### Constraints

- `1 <= nums.length <= 10⁴`
- `-2³¹ <= nums[i] <= 2³¹ - 1`

## Solution: Two-Pointer Swap

The solution uses a **two-pointer** technique to solve the problem in a single pass:

- `zero_pos` — tracks the position where the next non-zero element should be placed.
- `i` — iterates through every element in the array.

Whenever a non-zero element is found at index `i`, it is swapped with the element at `zero_pos`, and `zero_pos` is incremented. This ensures all non-zero elements bubble to the front in their original order, while zeros naturally drift to the end.

### Walkthrough

```
nums = [0, 1, 0, 3, 12]

i=0  nums[0]=0  → skip                 [0, 1, 0, 3, 12]  zero_pos=0
i=1  nums[1]=1  → swap(1,0), zero_pos++ [1, 0, 0, 3, 12]  zero_pos=1
i=2  nums[2]=0  → skip                 [1, 0, 0, 3, 12]  zero_pos=1
i=3  nums[3]=3  → swap(3,1), zero_pos++ [1, 3, 0, 0, 12]  zero_pos=2
i=4  nums[4]=12 → swap(4,2), zero_pos++ [1, 3, 12, 0, 0]  zero_pos=3
```

## Complexity Analysis

| Metric | Value |
|---|---|
| **Time** | O(n) — single pass through the array |
| **Space** | O(1) — in-place, no extra storage |
