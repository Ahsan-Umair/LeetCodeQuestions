# 232. Implement Queue using Stacks

## Problem

Implement a first-in-first-out queue using only stack operations.

## Approach

Use two stacks. New elements are pushed onto `stack1`. When `stack2` is empty, transfer all elements from `stack1` to `stack2`; this reverses their order so the oldest element is available at the top of `stack2`. `pop` and `peek` then operate on `stack2`, while `empty` checks both stacks.

## Complexity

- Time: `O(1)` amortized for `push`, `pop`, and `peek`; a transfer can take `O(n)` in one operation
- Time: `O(1)` for `empty`
- Space: `O(n)`, where `n` is the number of queued elements

## Solution

- [232-Implement-Queue-Using-Stack.py](./232-Implement-Queue-Using-Stack.py)
