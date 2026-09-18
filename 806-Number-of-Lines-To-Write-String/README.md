# 806. Number of Lines to Write String

## Problem

Given the width of each lowercase letter, determine how many lines are needed to write a string with a maximum width of 100 units per line and report the final line's width.

## Approach

The solution scans the string while tracking the current line width. A character is added when it fits; otherwise, a new line begins with that character.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [806-Number-of-Lines-To-Write-String.py](./806-Number-of-Lines-To-Write-String.py)
