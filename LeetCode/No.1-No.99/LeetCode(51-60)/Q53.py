class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return []
        pos = sofar = nums[0]
        for i in range(1, len(nums)):
            pos = max( nums[i] ,pos + nums[i] )
            sofar = max ( sofar , pos)
        return sofar

print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])