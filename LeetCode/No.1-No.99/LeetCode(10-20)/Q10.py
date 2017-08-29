class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s) , len(p)
        dp = [ [ False for __ in range(n+1)] for __ in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] | dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[m][n]

class Solution2(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for i in range(m + 1)]
        dp[m][n] = True
        for i in range(n - 1, -1, -1):
            if p[i] == "*":
                dp[m][i] = dp[m][i + 1]
            elif i + 1 < n and p[i + 1] == "*":
                dp[m][i] = dp[m][i + 1]
            else:
                dp[m][i] = False
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # When the current character is "*"
                if p[j] == "*":
                    if j - 1 >= 0 and p[j - 1] != "*":
                        dp[i][j] = dp[i][j + 1]
                    # If the pattern is starting with "*" or has "**" in it
                    else:
                        return False
                # When the the second character of pattern is "*"
                elif j + 1 < n and p[j + 1] == "*":

                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i][j + 2] or dp[i + 1][j] or dp[i + 1][j + 2]

                    else:
                        dp[i][j] = dp[i][j + 2]
                else:
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        dp[i][j] = False
        return dp[0][0]
if __name__== "__main__":
    print Solution().isMatch("aa", "a")
    print Solution().isMatch("aa", "aa")
    print Solution().isMatch("aaa", "aa")
    print Solution().isMatch("aa", "a*")
    print Solution().isMatch("aa", ".*")
    print Solution().isMatch("ab", ".*")
    print Solution().isMatch("aab", "c*a*b")
    print Solution().isMatch("", "")
    print Solution().isMatch("aaa", "ab*a*c*a")
