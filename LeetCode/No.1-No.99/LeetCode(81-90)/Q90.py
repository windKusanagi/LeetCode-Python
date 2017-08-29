class Solution(object):
    def subsetsWithDup(self, nums):

        result = [[]]
        nums.sort()
        temp_size = 0
        for i in range(len(nums)):
            start = temp_size if i >= 1 and nums[i] == nums[i - 1] else 0
            temp_size = len(result)
            for j in range(start, temp_size):
                result.append(result[j] + [nums[i]])
        return result
print Solution().subsetsWithDup([1, 2, 2])