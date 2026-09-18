# 125. Valid Palindrome — Two Pointers

## Problem

Determine whether a string is a palindrome after ignoring non-alphanumeric characters and letter case.

## Approach

The solution first builds a lowercase list of alphanumeric characters. Two pointers then compare characters from the beginning and end, moving inward until a mismatch is found or the pointers meet.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

- [Valid-Palindrome.py](./Valid-Palindrome.py)
