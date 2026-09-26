# 1621. Number of Sets of K Non-Overlapping Line Segments

## Problem

Given `n` points on a line, count the ways to draw exactly `k` non-overlapping line segments whose endpoints are chosen from those points. Segments may share an endpoint, and the answer is returned modulo `1,000,000,007`.

## Approach

The solution uses dynamic programming. `dp[j][i]` stores the number of ways to place `j` segments using points through index `i`. A running prefix sum collects the valid states from the previous segment count, avoiding an extra inner loop when choosing the start of the newest segment.

## Complexity

- Time: `O(n × k)`
- Space: `O(n × k)`

## Solution

- [1621. Number of Sets of K Non-Overlapping Line Segments.py](./1621.%20Number%20of%20Sets%20of%20K%20Non-Overlapping%20Line%20Segments.py)
