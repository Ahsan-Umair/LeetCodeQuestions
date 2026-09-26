# Fizz Buzz

## Problem

Given an integer `n`, return a list of strings for the numbers from `1` to `n`:

- Multiples of both `3` and `5` become `"FizzBuzz"`.
- Multiples of `3` become `"Fizz"`.
- Multiples of `5` become `"Buzz"`.
- All other numbers become their string representation.

## Approach

Iterate from `1` through `n` once. Check divisibility by both `3` and `5` first, then check each divisor individually. Append the appropriate value to the result list.

## Complexity

- Time: `O(n)`
- Space: `O(n)` for the returned list

## Implementation

See [412-Fizz Buzz.py](412-Fizz%20Buzz.py).
