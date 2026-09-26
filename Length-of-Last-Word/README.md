# 58. Length of Last Word

## Problem

Return the length of the final word in a string that may contain trailing spaces.

## Approach

The index moves backward past trailing spaces, then continues backward while counting characters until another space or the beginning of the string is reached.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Length-of-Last-Word.py](./Length-of-Last-Word.py)
