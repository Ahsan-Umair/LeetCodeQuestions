class Solution:
    def findComplement(self, num: int) -> int:
        answer = ""
        binary = bin(num)[2:]

        bits = num.bit_length()

        mask = (1<<bits) - 1

        return num ^ mask