class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(n):
            dp[0][i] = 1

        for j in range(1, k + 1):
            prefix = 0
            for i in range(1, n):
                prefix = (prefix + dp[j - 1][i - 1]) % MOD
                dp[j][i] = (dp[j][i - 1] + prefix) % MOD

        return dp[k][n - 1]