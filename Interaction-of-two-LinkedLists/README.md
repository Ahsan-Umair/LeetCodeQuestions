# 160. Intersection of Two Linked Lists

## Problem

Return the node where two singly linked lists intersect, or `None` when they do not intersect.

## Approach

Two pointers traverse the lists. After reaching the end of its original list, each pointer switches to the other list's head. This equalizes the total distance traveled, causing the pointers to meet at the intersection or at `None`.

## Complexity

- Time: `O(m + n)`
- Space: `O(1)`

## Solution

- [Interaction-of-two-LinkedLists.py](./Interaction-of-two-LinkedLists.py)
