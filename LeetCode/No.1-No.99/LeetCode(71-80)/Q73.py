class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        firstRow, firstCol = 1, 1
        for i in range(n):
            if matrix[0][i] == 0:
                firstRow = 0
                break
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = 0
                break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0 :
                    matrix[i][j] = 0
        if firstRow == 0:
            for i in range(n):
                matrix[0][i] = 0
        if firstCol == 0:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

matrix = [[1, 0, 1, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 0],
          [1, 1, 1, 1]]
print Solution().setZeroes(matrix)