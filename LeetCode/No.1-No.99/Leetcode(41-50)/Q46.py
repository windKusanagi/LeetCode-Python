class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current+[])
            return
        for i, v in enumerate(num):
            #current.append(num[i])
            self.get_permute(current + [num[i]], num[:i] + num[i + 1:], result)
            #current.pop()

print Solution().permute([1, 2, 3])