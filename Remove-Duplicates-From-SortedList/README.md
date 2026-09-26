# 83. Remove Duplicates from Sorted List

## Problem

Remove duplicate values from a sorted singly linked list and return its head.

## Approach

The current node is compared with its successor. Equal successors are skipped by redirecting `current.next`; otherwise, the current pointer advances.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Remove-Duplicates-From-SortedList.py](./Remove-Duplicates-From-SortedList.py)
