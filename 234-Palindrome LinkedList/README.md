# 234. Palindrome Linked List

## Problem

Determine whether a singly linked list reads the same from left to right and
right to left.

## Approach

The solution uses the fast and slow pointer technique to locate the midpoint
of the list. It then reverses the second half in place and compares that
reversed half with the list's first half. Any different pair of values means
the list is not a palindrome; if every value matches, it is a palindrome.

The linked list is modified while the second half is reversed and is not
restored afterward.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [234-Palindrome-LinkedList.py](./234-Palindrome-LinkedList.py)
