# 506. Relative Ranks

## Problem

Assign medal labels to the three highest scores and numeric rank strings to all remaining athletes while preserving the original input order.

## Approach

Each score is paired with its original index and sorted from highest to lowest. The sorted position determines the rank label, which is written into an answer array at the saved original index.

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Solution

- [506-Relative-Ranks.py](./506-Relative-Ranks.py)
