# 832. Flipping an Image

## Problem

Horizontally flip each row of a binary image and then invert every bit.

## Approach

Each row is reversed with slicing. The reversed row is scanned and every `0` is changed to `1`, while every `1` is changed to `0`, before the row is appended to the result.

## Complexity

- Time: `O(rows × columns)`
- Space: `O(rows × columns) for the returned image`

## Solution

- [832-Flipping-An-Image.py](./832-Flipping-An-Image.py)
