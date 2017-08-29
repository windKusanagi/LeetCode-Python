class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [0 for __ in range(n)]
        isPal = [[False for __ in range(n)] for __ in range(n)]
        for i in range(n):
            m = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    m = 0 if j == 0 else min(m, dp[j - 1] + 1)
            dp[i] = m
        print isPal[0]
        print isPal[1]
        print isPal[2]
        print isPal[3]
        print isPal[4]
        return dp[-1]

print Solution().minCut("abcbm")