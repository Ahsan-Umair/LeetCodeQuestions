# 27. Remove Element

## Problem

Remove every occurrence of a target value from an array in place and return the number of retained elements.

## Approach

A fast pointer scans every value while a slow pointer marks the next output position. Values different from the target are copied to the slow position, which then advances.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Remove-Element.py](./Remove-Element.py)
