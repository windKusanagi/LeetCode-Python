class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        length = 1
        prev = 0
        cur = 1
        while cur<= len(nums)-1:
            if nums[cur] != nums[prev]:
                nums[length] = nums[cur]
                length+=1;
                prev = cur;
                cur += 1;
            else:
                cur += 1
        return length

nums1 = [1, 1, 2,2,2,2,2,3,4,4,5]
print Solution().removeDuplicates(nums1)
print nums1


