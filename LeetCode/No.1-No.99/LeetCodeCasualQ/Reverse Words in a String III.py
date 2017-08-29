class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        collect = s.split(" ")
        result=[]
        for i in range(len(collect)):
            result.append(collect[i][::-1])
        return " ".join(result)

print Solution().reverseWords(" Let's take LeetCode contest")