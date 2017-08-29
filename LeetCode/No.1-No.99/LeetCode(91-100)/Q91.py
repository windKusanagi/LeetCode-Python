class Solution(object):
    def numDecodings(self, s):
        if not s or not s[0].isdigit() or s[0] == '0':
            return 0
        dp = [ 0 for __ in range(len(s) + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(1,len(s)):
            if not s[i].isdigit():
                return 0
            var = (ord(s[i-1])-ord('0'))*10 + ord(s[i])-ord('0')
            if var <= 26 and var > 9:
                dp[i+1] += dp[i-1]
            if s[i] != '0':
                dp[i+1] += dp[i]
            if dp[i+1] == 0:
                return 0
        return dp[-1]
print Solution().numDecodings("27")
