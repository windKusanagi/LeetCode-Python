class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"

        result = []
        while num and len(result) != 8:
            h = num & 15
            if h < 10:
                result.append(str(chr(ord('0') + h)))
            else:
                result.append(str(chr(ord('a') + h-10)))
            num >>= 4
        result.reverse()

        return "".join(result)

print Solution().toHex(-1)