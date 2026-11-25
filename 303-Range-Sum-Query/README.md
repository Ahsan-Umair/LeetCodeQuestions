# 303. Range Sum Query — Immutable

## Problem

Store an integer array and answer repeated queries for the sum of elements between two inclusive indices.

## Approach

The constructor builds a prefix-sum array with a leading zero. Each query subtracts `prefix[left]` from `prefix[right + 1]`, so the requested range sum is returned without scanning the range again.

## Worked example

For `nums = [3, -2, 4, 1]`, the constructor produces
`prefix = [0, 3, 1, 5, 6]`. Each `prefix[i]` sums the first `i` elements.
The prefix can decrease when the next value is negative.

| Query | Calculation | Sum |
|---|---|---:|
| `sumRange(1, 2)` | `prefix[3] - prefix[1] = 5 - 3` | 2 |
| `sumRange(0, 2)` | `prefix[3] - prefix[0] = 5 - 0` | 5 |
| `sumRange(1, 1)` | `prefix[2] - prefix[1] = 1 - 3` | -2 |

Using `right + 1` includes `nums[right]`. Subtracting `prefix[left]`
removes exactly the elements before `left`. The leading `0` lets the same
formula handle ranges that start at index zero.

## Complexity

- Time: `O(n) preprocessing and O(1) per query`
- Space: `O(n)`

## Solution

- [303-Range-Sum-Query.py](./303-Range-Sum-Query.py)
