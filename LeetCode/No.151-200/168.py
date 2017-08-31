class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = ord('A')
        result = []
        while n:
            n, r = divmod(n-1, 26)
            result.append(chr(base + r))

        return ''.join(result[::-1])

if __name__ =='__main__':
    print Solution().convertToTitle(28)