# 2472. Maximum Number of Non-overlapping Palindrome Substrings

## Problem

Find the maximum number of non-overlapping palindromic substrings of `s`, where every chosen substring has length at least `k`.

## Approach

The solution scans from left to right and greedily takes the earliest palindrome of length `k` or `k + 1`. When one is found, the index jumps past it; otherwise, the scan advances by one character.

## Complexity

- Time: `O(n × k) because each palindrome check slices and reverses up to `k + 1` characters`
- Space: `O(k) for temporary slices`

## Solution

- [2472-Max-Numbers-of-NonOverlapping-Palindrome-SubStrings.py](./2472-Max-Numbers-of-NonOverlapping-Palindrome-SubStrings.py)
