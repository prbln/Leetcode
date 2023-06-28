class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #lcs 
        m,n = len(word2), len(word1)
        dp = [[0]*(m+1 )for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    # print(i,j)
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return (m - dp[n][m]) + (n-dp[n][m])