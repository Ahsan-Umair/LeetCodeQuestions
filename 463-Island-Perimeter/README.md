# 463. Island Perimeter

## Problem

Given a binary grid containing land and water, calculate the perimeter of the island.

## Approach

Every land cell is inspected on all four sides. A perimeter edge is added whenever that side touches the grid boundary or a water cell.

## Complexity

- Time: `O(rows × columns)`
- Space: `O(1)`

## Solution

- [463-Island-Perimeter.py](./463-Island-Perimeter.py)
