class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        top = left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        result = []
        while left<=right and top <=bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            for i in range(top+1, bottom+1):
                result.append(matrix[i][right])
            for i in range(right-1, left-1, -1):
                if top < bottom:
                    result.append(matrix[bottom][i])
            for i in range(bottom-1, top, -1):
                if left < right :
                    result.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        return result

print Solution().spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])