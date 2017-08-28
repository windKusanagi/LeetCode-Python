class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = nums[0]
        for i in nums[1:]:
            single ^= i
        return single

if __name__ == "__main__":
    print Solution().singleNumber([1, 2, 3, 4, 5, 5, 3, 2, 1])
