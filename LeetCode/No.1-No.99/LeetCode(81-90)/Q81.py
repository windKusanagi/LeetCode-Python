class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
print Solution().search([4, 5, 5, 6, 7, 0, 1, 2], 4)
print Solution().search([4, 5, 6, 7, 7, 7, 7, 7, 0, 1, 2], 8)