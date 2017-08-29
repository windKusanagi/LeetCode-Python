class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n -1
        while l<=r :
            mid = l + (r-l)/2
            if matrix[mid/n] [mid%n] == target:
                return True
            if matrix[mid/n] [mid%n] > target:
                r = mid - 1
            else:
                l = mid + 1

print Solution().searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)