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

left=0, right=8  width=8, height=1  area=8   max_area=8
left=1, right=8  width=7, height=7  area=49  max_area=49
left=1, right=7  width=6, height=3  area=18  max_area=49
left=1, right=6  width=5, height=8  area=40  max_area=49
left=1, right=5  width=4, height=4  area=16  max_area=49
left=1, right=4  width=3, height=5  area=15  max_area=49
left=1, right=3  width=2, height=2  area=4   max_area=49
left=1, right=2  width=1, height=6  area=6   max_area=49
```

At `left=1, right=6`, both heights are `8`. The code moves `right` because
the left height is not strictly smaller. The pointers eventually meet at
index `1`, ending the loop. The maximum area found is `49`.

### Edge cases

- `[0, 0]` returns `0`, since neither line can hold water.
- `[1, 1]` returns `1`, the area of the only pair.
- `[3, 3, 3]` returns `6`, using the two outer lines for the largest width.

### Why a wall can be discarded

Suppose the left wall is shorter than or equal to the right wall. Any pair
that keeps this left wall and moves the right wall closer has less width,
while its usable height is at most the left wall's height. Such a pair cannot
beat the area just checked, so the left wall can be discarded safely. The
same argument applies to the right wall when it is shorter.

When both walls have equal height, either wall can be discarded for this
reason. This implementation chooses to move `right` in that case.

## Complexity

- **Time:** `O(n)` — each pointer moves across the array at most once.
- **Space:** `O(1)` — only pointer and area variables are used.

## Solution

- [11-Container-With-Most-Water.py](./11-Container-With-Most-Water.py)
