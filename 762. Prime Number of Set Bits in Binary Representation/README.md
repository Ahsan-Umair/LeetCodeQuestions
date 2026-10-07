# 762. Prime Number of Set Bits in Binary Representation

## Problem

Given two integers `left` and `right`, count the integers in the inclusive range `[left, right]` whose number of set bits (bits equal to `1` in their binary representation) is prime.

For example, `10` is `1010` in binary and has two set bits. Since `2` is prime, `10` contributes to the answer.

## Approach

The `Solution.countPrimeSetBits` method:

1. Iterates over every number from `left` through `right`.
2. Converts each number to binary with `bin(num)[2:]`.
3. Counts the `1` characters in the binary representation.
4. Checks whether the set-bit count is prime by trying possible divisors from `2` through `set_bits - 1`.
5. Increments the result when the set-bit count is prime.

Set-bit counts below `2` are treated as non-prime.

## Complexity

Let `n = right - left + 1` and let `b` be the maximum number of bits in the numbers being checked.

- **Time:** `O(n * (b + b))` in the worst case, or `O(n * b)` when `b` is treated as the machine/input bit width. The first `b` term is for binary conversion and counting; the second is for the trial-division prime check.
- **Space:** `O(b)` for the binary representation of one number.

## Usage

```python
solution = Solution()
answer = solution.countPrimeSetBits(left, right)
```

The implementation is contained in [`762. Prime Number of Set Bits in Binary Representation.py`](./762.%20Prime%20Number%20of%20Set%20Bits%20in%20Binary%20Representation.py).
