# 228. Summary Ranges

## Problem

Given a sorted array of unique integers, summarize each consecutive range as
either a single value or a range from its first value to its last value.

## Approach

The solution tracks the start index of the current consecutive range. As the
array is scanned, a break is found whenever the next value is not one greater
than the previous value. The completed range is then formatted and the start
index is moved to the new range. The final range is appended after the scan.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the result

## Solution

- [228-Summary-ranges.py](./228-Summary-ranges.py)
