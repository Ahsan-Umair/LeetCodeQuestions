class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []

        for i in range(n+1):
            num = i
            count = 0

            while num !=0:
                last_bit = num & 1
                num >>= 1

                count += last_bit
            ans.append(count)

        return ans
