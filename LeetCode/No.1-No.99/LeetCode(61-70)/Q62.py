'''
class Solution(object):
    def uniquePaths(self, m, n):
        dp =[ [0 for __ in range(n)]for __ in range(m)]
        dp [0][0] = 1
        for i in range(m):
            for j in range(n):
                if i+1 < m:
                    dp[i+1][j] += dp[i][j]
                if j+1 < n:
                    dp[i][j+1] += dp[i][j]
        return dp[m-1][n-1]
'''
class Solution(object):
    def uniquePaths(self, m, n):
        dp =[ [0 for __ in range(n)]for __ in range(m)]
        dp [0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

print Solution().uniquePaths(3, 7)