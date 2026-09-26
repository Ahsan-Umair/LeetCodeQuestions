# 141. Linked List Cycle

## Problem

Determine whether a singly linked list contains a cycle.

## Approach

Floyd's tortoise-and-hare algorithm advances one pointer by one node and another by two nodes. If they meet, the list has a cycle; if the fast pointer reaches the end, it does not.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [LinkedList-Cycle.py](./LinkedList-Cycle.py)
