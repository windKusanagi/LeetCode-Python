class Solution(object):
    def generateMatrix(self, n):
        top = left = 0
        bottom = n-1
        right = n-1
        num1 = 1
        result = [ [0 for __ in range(n)] for __ in range(n)]
        while left<=right and top <=bottom:
            for i in range(left, right+1):
                result[top][i] = num1
                num1+=1
            for i in range(top+1, bottom+1):
                result[i][right] = num1
                num1+=1
            for i in range(right-1, left-1, -1):
                if top < bottom:
                    result[bottom][i] = num1
                    num1+=1
            for i in range(bottom-1, top, -1):
                if left < right :
                    result[i][left] = num1
                    num1+=1
            left+=1
            right-=1
            top+=1
            bottom-=1
        return result
print Solution().generateMatrix(3)