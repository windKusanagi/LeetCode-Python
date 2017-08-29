class Solution(object):
    def grayCode(self, n):
        result = [0]
        for i in xrange(n):
            for n in reversed(result):
                result.append(1 << i | n)
        return result

print Solution().grayCode(2)