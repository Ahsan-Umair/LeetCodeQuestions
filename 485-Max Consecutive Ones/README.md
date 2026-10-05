# 485. Max Consecutive Ones

## Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

### Examples

| Input | Output |
|---|---|
| `[1, 1, 0, 1, 1, 1]` | `3` |
| `[1, 0, 1, 1, 0, 1]` | `2` |

## Approach

The solution scans the array once while maintaining two counters:

- `current_count` — the length of the consecutive run of `1`s ending at the current position.
- `max_count` — the longest run found so far.

For each element:

- Increment `current_count` when the element is `1`.
- Reset `current_count` to `0` when the element is `0`.
- Update `max_count` with the longest run seen so far.

Because a zero ends the current run, resetting the running counter lets the algorithm start counting the next sequence of ones immediately.

### Walkthrough

```text
nums = [1, 1, 0, 1, 1, 1]

value=1  current_count=1  max_count=1
value=1  current_count=2  max_count=2
value=0  current_count=0  max_count=2
value=1  current_count=1  max_count=2
value=1  current_count=2  max_count=2
value=1  current_count=3  max_count=3
```

The longest consecutive run contains `3` ones.

## Complexity

- **Time:** `O(n)` — each element is visited once.
- **Space:** `O(1)` — only two counters are used.

## Solution

- [485-Max-Consecutive-Ones.py](./485-Max-Consecutive-Ones.py)
