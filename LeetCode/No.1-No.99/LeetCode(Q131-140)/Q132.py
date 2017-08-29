class Solution(object):
    def minCut(self, s):
        dp = [[0 for __ in range(len(s))] for __ in range(len(s))]
        n = len(s)
        for length in range(1, n):
            for i in range( n-length):
                j = i+length
                if self.isPal(s[i:j+1]):
                    dp[i][j] = 0
                else:
                    temp = 2**16-1
                    for k in range(i,j):
                        temp = min (temp , dp[i][k] + dp[k+1][j])
                    dp[i][j] = 1+temp
        return dp[0][-1]
    def isPal (self, s):
        return s == s[::-1]


if __name__ == "__main__":
    print Solution().minCut("abcbm")
    print Solution().minCut("aab")