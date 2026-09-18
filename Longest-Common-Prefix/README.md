# 14. Longest Common Prefix

## Problem

Find the longest prefix shared by every string in an array.

## Approach

The shortest string length limits the possible prefix. For each position up to that length, the solution compares the first string's character with the character at the same position in every other string and returns at the first mismatch.

## Complexity

- Time: `O(S), where `S` is the number of inspected characters`
- Space: `O(k) for the list of `k` string lengths`

## Solution

- [Longest-Common-Prefix.py](./Longest-Common-Prefix.py)
