class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left != right:
            if numbers[right] + numbers[left] > target:
                right -= 1

            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 15], 18)
