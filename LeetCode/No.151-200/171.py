class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        result = 0
        base = ord('A') - 1
        for i in range(length):
            result += (ord(s[i]) - base) * pow(26, length-i-1)
        return result

if __name__ == '__main__':
    print Solution().titleToNumber('AB')