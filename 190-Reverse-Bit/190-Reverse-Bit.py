class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        bit = binary.zfill(32)
        reversed_32_bit = bit[::-1]
        decimal_binary = int(reversed_32_bit,2)

        return decimal_binary
