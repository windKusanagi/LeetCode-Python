class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        maxReach = nums[0]
        pos = 0
        while pos < len(nums):
            if maxReach < pos:
                return False
            else:
                if maxReach < nums[pos]+pos:
                    maxReach = nums[pos]+pos
                pos+=1
        return True
print Solution().canJump([3, 2, 1, 0, 4])
