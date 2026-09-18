# 206. Reverse Linked List

## Problem

Reverse a singly linked list and return the new head.

## Approach

Three references are used while walking through the list: `current` points to the node being processed, `prev` points to the already-reversed portion, and `temp` preserves the next node before the link is reversed.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [206-Reversed-LinkedList.py](./206-Reversed-LinkedList.py)
