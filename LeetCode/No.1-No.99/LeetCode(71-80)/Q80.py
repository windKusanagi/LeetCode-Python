class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums)<=2:
            return len(nums)
        length = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[length-2]:
                nums[length] = nums[i]
                length += 1
        return length

l = [1, 1, 1, 2, 2, 3]
r = Solution().removeDuplicates(l)
print r
print l
