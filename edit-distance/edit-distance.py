class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) 
        m = len(word2)
        dp = [[0]*(m+1)for _ in range(n+1)]
        dp[0][0] = 0 
        for i in range(0,n+1):
            for j in range(0,m+1):
                if i ==0:
                    dp[0][j] = j
                    continue
                if j ==0:
                    dp[i][0] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =  dp[i-1][j-1]
                else:
                    dp[i][j] = min(1+dp[i-1][j], 1+dp[i][j-1], 1+dp[i-1][j-1])
        # print(dp)
        return dp[n][m]

        