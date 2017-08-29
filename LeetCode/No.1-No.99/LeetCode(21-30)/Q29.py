'''
class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2**31-1
        flag = 1
        if (dividend >= 0 and divisor < 0) or (dividend <= 0 and divisor > 0):
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        return min(flag * res, MAX_INT)

print Solution().divide(50, -1)
'''

class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2**31-1
        flag = 1
        if (dividend >= 0 and divisor < 0) or (dividend<=0 and divisor>0):
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            cur = divisor
            count = 1
            while dividend >= cur:
                dividend-= cur
                res += count
                cur <<= 1
                count <<= 1
        return min(flag*res , MAX_INT)

print Solution().divide(50, -1)