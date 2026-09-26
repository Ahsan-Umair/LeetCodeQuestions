# 190. Reverse Bits

## Problem

Reverse bits of a given 32 bits unsigned integer.

**Note:** In some languages, there is no unsigned integer type. The input will be given as a signed integer, but the integer's internal binary representation is the same regardless.

### Examples

| Input | Output |
|---|---|
| `00000010100101000001111010011100` | `964176192` (`00111001011110000010100101000000`) |
| `11111111111111111111111111111101` | `3221225471` (`10111111111111111111111111111111`) |

### Constraints

- The input must be a **binary string** of length `32`.

## Solution: String-Based Bit Reversal

The solution converts the integer to its 32-bit binary string representation, reverses the string, and converts it back to a decimal integer:

1. **Convert to binary** — `bin(n)[2:]` strips the `0b` prefix.
2. **Zero-fill to 32 bits** — `.zfill(32)` pads with leading zeros so the result is always 32 bits wide.
3. **Reverse the string** — `[::-1]` produces the reversed bit pattern.
4. **Convert back to decimal** — `int(reversed_str, 2)` parses the reversed binary string as base-2.

### Walkthrough

```
n = 43261596

bin(43261596)        → '0b10100100111110010100011000'
[2:]                 → '10100100111110010100011000'
.zfill(32)           → '00000010100101000001111010011100'
[::-1]               → '00111001011110000010100101000000'
int(..., 2)          → 964176192
```

## Complexity Analysis

| Metric | Value |
|---|---|
| **Time** | O(1) — always operates on a fixed 32-bit string |
| **Space** | O(1) — uses a constant-size 32-character string |
