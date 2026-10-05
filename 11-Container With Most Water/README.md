# 11. Container With Most Water

## Problem

Given an array `height` where `height[i]` represents the height of a vertical line at position `i`, choose two lines that together with the x-axis form a container. Return the maximum amount of water the container can store.

The container's area is determined by:

```text
width × min(left_height, right_height)
```

### Examples

| Input | Output |
|---|---|
| `[1, 8, 6, 2, 5, 4, 8, 3, 7]` | `49` |
| `[1, 1]` | `1` |

### Constraints

- `2 <= height.length <= 10⁵`
- `0 <= height[i] <= 10⁴`

## Approach: Two Pointers

Start with one pointer at each end of the array:

- `left` points to the first line.
- `right` points to the last line.

At each step, calculate the area formed by the two lines and update `max_area`. Then move the pointer at the shorter line inward:

- If the left line is shorter, increment `left`.
- Otherwise, decrement `right`.

The shorter line limits the container's height. Moving the taller line would reduce the width without providing a taller limiting wall, so it cannot produce a better area.

### Walkthrough

```text
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left=0, right=8  width=8, height=1  area=8
left=1, right=8  width=7, height=7  area=49
```

The maximum area found is `49`.

## Complexity

- **Time:** `O(n)` — each pointer moves across the array at most once.
- **Space:** `O(1)` — only pointer and area variables are used.

## Solution

- [11-Container-With-Most-Water.py](./11-Container-With-Most-Water.py)
