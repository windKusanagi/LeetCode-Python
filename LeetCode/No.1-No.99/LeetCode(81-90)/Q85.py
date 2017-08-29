class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        height = [0 for __ in range(len(matrix[0]) + 1)]
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                height[j] = height[j]+1 if matrix[i][j] == '1' else 0
            stack = [-1]
            for k in range(len(height)):
                while height[k] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = k-1 - stack[-1]
                    result = max ( result, h*w)
                stack.append(k)
        return result

print Solution().maximalRectangle(     [['1', '1', '0', '1', '0', '1'],
                                        ['0', '1', '0', '0', '1', '1'],
                                        ['1', '1', '1', '1', '0', '1'],
                                        ['1', '1', '1', '1', '0', '1']])