class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len( matrix )
        for i in range (length):
            for j in range(length - i):
                matrix[i][j], matrix[length-1-j][length-1-i] = matrix[length-1-j][length-1-i], matrix[i][j]

        for i in range(length/2):
            for j in range(length):
                matrix[i][j], matrix[length-1-i][j] = matrix[length-1-i][j], matrix[i][j]

        return matrix

print Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]])