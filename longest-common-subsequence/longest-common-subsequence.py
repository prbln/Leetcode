class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text2), len(text1)
        dp = [[0]*(m+1 )for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    # print(i,j)
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]
