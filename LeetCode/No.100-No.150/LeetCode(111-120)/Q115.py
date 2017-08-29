class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t)+1 , len(s)+1
        if m>n:
            return 0
        dp = [ [0 for __ in range(n)] for __ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m):
            dp[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if t[i-1] != s[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        return dp[m-1][n-1]
S = "rabbbit"
T = "rabbit"
result = Solution().numDistinct(S, T)
print result