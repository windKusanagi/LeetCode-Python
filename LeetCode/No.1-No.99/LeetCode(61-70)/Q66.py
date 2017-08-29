class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        else:
            digits[-1] = 0
            carry = 1
            for i in range( len(digits)-2 ,-1, -1):
                if digits[i] + carry == 10:
                    digits[i] = 0
                else:
                    digits[i] += carry;
                    carry = 0
            if carry == 1:
                digits = [1]+digits
            return digits
print  Solution().plusOne([1, 2, 3, 4, 9])
print Solution().plusOne([9])
print Solution().plusOne([0])