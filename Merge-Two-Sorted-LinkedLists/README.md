# 21. Merge Two Sorted Lists

## Problem

Merge two sorted singly linked lists and return one sorted list.

## Approach

A dummy head simplifies construction. The smaller front node is repeatedly linked to the result, and once one input is exhausted, the unprocessed remainder of the other list is attached.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Solution

- [Merge-Two-Sorted-LinkedLists.py](./Merge-Two-Sorted-LinkedLists.py)
