# 121. Best Time to Buy and Sell Stock

## Problem

Choose one day to buy and a later day to sell a stock so that profit is maximized.

## Approach

The solution scans prices once while maintaining the lowest price seen so far. At every later price, it computes the profit from selling there and keeps the largest profit.

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Solution

- [Best-Time-To-Buy&Sell-Stock.py](./Best-Time-To-Buy%26Sell-Stock.py)
