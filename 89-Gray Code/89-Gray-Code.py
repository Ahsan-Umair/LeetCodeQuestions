class Solution:
    def grayCode(self, n: int) -> list[int]:
        gray = [0]

        for i in range(n):
            for x in reversed(gray):
                gray.append(x + (1 << i))
        return gray