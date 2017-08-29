class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if len(s3) != m+n:
            return False
        dp = [[0 for __ in range(m+1)] for __ in range(n+1)]
        dp [0][0] = True
        for i in range(1, m+1):
            if s3[i-1] == s1[i-1] and dp[0][i-1] == True:
                dp[0][i] = True
            else:
                dp[0][i] = False
        for i in range(1, n+1):
            if s3[i-1] == s2[i-1] and dp[i-1][0] == True:
                dp[i][0] = True
            else:
                dp[i][0] = False
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s3[i+j-1] == s1[j-1] and dp[i][j-1] == True:
                    dp[i][j] = True
                elif s3[i+j-1] == s2[i-1] and dp[i-1][j] == True:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[n][m]

print Solution().isInterleave("aab", "axy", "aaxaby")
print Solution().isInterleave("aab", "axy", "abaaxy")
print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")