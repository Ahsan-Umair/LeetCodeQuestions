# Valid Palindrome — List and Reverse Approach

## Problem

Determine whether a string is a palindrome after ignoring non-alphanumeric characters and letter case.

## Approach

This implementation builds a lowercase list containing only alphanumeric characters, then compares that list with a reversed copy. Despite the folder name, the code checks an exact cleaned palindrome and does not remove a mismatching character.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Solution

- [Valid-Palindrome-II.py](./Valid-Palindrome-II.py)
