class Solution(object):
    def searchRange(self, nums, target):
        result = []
        start, end = 0 , len(nums)
        while start < end:
            mid = (start+end)/2
            if nums[mid] == target and (mid==0 or nums[mid-1] != target  ):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid
        if len(result)==0:
            return [-1,-1]

        start, end = 0 , len(nums)
        while start < end:
            mid = (start+end)/2
            if nums[mid] == target and (mid==end-1 or nums[mid+1] != target):
                result.append(mid)
                break
            if nums[mid] <= target:
                start = mid+1
            else:
                end = mid
        return result

num1 = [1]
print Solution().searchRange(num1 , 0)