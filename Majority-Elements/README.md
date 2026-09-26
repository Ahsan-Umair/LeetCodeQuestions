# 169. Majority Element

## Problem

Return the element that appears more than half the time in the array.

## Approach

After sorting, the majority element must occupy the middle index, so the solution returns `nums[n // 2]`.

## Complexity

- Time: `O(n log n)`
- Space: `O(n) worst-case auxiliary space for Python's sort`

## Solution

- [Majority-Elements.py](./Majority-Elements.py)
