class Solution(object):
    def isPalindrome(self, s):
        str1 = [item for item in s.lower() if item.isalnum()]
        return str1 == str1[::-1]
print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome("race a car")
print Solution().isPalindrome("0P")
print Solution().isPalindrome(" ")
print Solution().isPalindrome("..   ")