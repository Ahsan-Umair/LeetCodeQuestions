# 225. Implement Stack Using Queues

## Problem

Implement a last-in, first-out stack using only queue-style operations. The stack must support `push`, `pop`, `top`, and `empty`.

## Approach

The solution maintains two queues, `q1` and `q2`, represented by Python lists. New values are appended to `q1`. For `pop`, all but the final value are moved from `q1` to `q2`; the remaining value is removed and returned as the top of the stack, and the queue references are swapped. The `top` operation performs the same transfer but places the final value into `q2` before swapping so it remains in the stack. The stack is empty when `q1` has no elements.

## Complexity

- `push`: `O(1)` amortized
- `empty`: `O(1)`
- `pop` and `top`: `O(n²)` with Python lists because every `pop(0)` shifts the remaining elements. With `collections.deque`, the same two-queue algorithm would take `O(n)`.
- Space: `O(n)`

## Solution

- [225-Implement-Stack-Using-Queues.py](./225-Implement-Stack-Using-Queues.py)
