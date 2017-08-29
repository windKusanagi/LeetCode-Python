class Solution(object):
    def mySqrt(self, x):
        result = 1.0
        while abs(result * result - x) > 0.1:
            result = (result + x / result) / 2
        return int(result)

print Solution().mySqrt(5)