class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0 for __ in range(n+1)]
        count[0] = 1
        count[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                count[i] += count[j]*count[i-j-1]

        return count[n]
print Solution().numTrees(5)