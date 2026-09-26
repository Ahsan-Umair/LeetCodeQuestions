# 119. Pascal's Triangle II

## Problem

Return the row at the requested zero-based index of Pascal's triangle.

## Approach

Starting from `[1]`, the solution builds each next row from adjacent pairs in the current row, then adds `1` at both ends. Only the current and next rows are retained.

## Complexity

- Time: `O(r²)`
- Space: `O(r)`

## Solution

- [Pascal's-Triangle-II.py](./Pascal's-Triangle-II.py)
