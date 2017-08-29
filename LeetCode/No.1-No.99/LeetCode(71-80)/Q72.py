class Solution(object):
    def minDistance(self, word1, word2):

        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for __ in range(l2+1)] for __ in range(l1+1)]
        for i in range (l2+1):
            dp[0][i] = i
        for i in range (l1+1):
            dp[i][0] = i
        for i in range( 1, l1+1):
            for j  in range( 1, l2+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i-1][j] , dp[i][j-1], dp[i-1][j-1] ) +1
        return dp[l1][l2]
print Solution().minDistance("azced", "abcdef")
