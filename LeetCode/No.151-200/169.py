class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, result = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] != result:
                count -= 1
            else:
                count += 1
            if count == 0:
                result = nums[i]
                count = 1
        return result

if __name__ == '__main__':
    print Solution().majorityElement([3, 2, 3, 5, 6, 7, 8, 5, 9, 3, 4, 5, 1, 3, 5, 5, 6, 5])
