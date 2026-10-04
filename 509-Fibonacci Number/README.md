# 509. Fibonacci Number

## Problem

The Fibonacci numbers, commonly denoted `F(n)`, form a sequence such that each number is the sum of the two preceding ones, starting from `0` and `1`.

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1
```

Given `n`, calculate `F(n)`.

**Link:** [LeetCode 509 – Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## Approach — Top-Down DP (Memoization)

The solution uses **recursion with memoization** to avoid redundant calculations:

1. A dictionary `d` is initialized with the base cases `{0: 0, 1: 1}`.
2. A recursive helper `fibonacci(n, d)` checks if `n` is already in the dictionary (cache hit) and returns it directly.
3. Otherwise, it computes `F(n) = F(n-1) + F(n-2)`, stores the result in `d`, and returns it.

This converts the naive exponential recursion into an efficient linear pass.

## Complexity

| Metric | Value |
|--------|-------|
| **Time**  | O(n) |
| **Space** | O(n) |

## Code

```python
class Solution:
    def fib(self, n: int) -> int:
        d = {0: 0, 1: 1}

        def fibonacci(n, d):
            if n in d:
                return d[n]
            else:
                d[n] = fibonacci(n - 1, d) + fibonacci(n - 2, d)
                return d[n]

        return fibonacci(n, d)
```
