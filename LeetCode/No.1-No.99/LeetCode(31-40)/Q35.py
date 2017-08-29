class Solution(object):
    def searchInsert(self, nums, target):
        result = -1
        start, end = 0, len(nums)
        while start < end:
            mid = (start+end)/2
            if nums[mid] == target:
                return mid
            elif mid==0 and nums[mid]>target:
                return mid
            elif mid == end -1 and nums[mid]<target:
                return mid+1
            elif nums[mid]< target and nums[mid +1]> target :
                return mid+1
            elif nums[mid]< target:
                start = mid+1
            else:
                end = mid
print Solution().searchInsert([1], 2)