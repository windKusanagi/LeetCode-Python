class Solution(object):
    def subsets(self, nums):
        result = [[]]
        self.subsetBK(sorted(nums), result, 0, [])
        return result

    def subsetBK(self, nums, result, start, current):
        for i in range(start, len(nums)):
            current.append(nums[i])
            result.append(current+[])
            self.subsetBK(nums, result, i + 1, current)
            current.pop()

print Solution().subsets([1, 2, 2])