# 118. Pascal's Triangle

## Problem

Generate the first `numRows` rows of Pascal's triangle.

## Approach

Each row begins filled with ones. Interior values are calculated by adding the two values directly above them in the previous row, and every completed row is appended to the triangle.

## Complexity

- Time: `O(numRows²)`
- Space: `O(numRows²) for the returned triangle`

## Solution

- [Pascal's-Triangle.py](./Pascal's-Triangle.py)
