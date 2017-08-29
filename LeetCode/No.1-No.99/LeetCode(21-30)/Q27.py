class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        length = 0
        prev = 0
        cur = 0
        while cur<= len(nums)-1:
            if nums[cur] != val:
                nums[length] = nums[cur]
                length+=1;
                prev = cur;
                cur += 1;
            else:
                cur += 1
        return length

nums1 = [2,2,2]

print Solution().removeElement(nums1, 0)
print nums1


