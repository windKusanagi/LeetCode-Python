class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [-1]
        heights.append(0)
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-1 - stack[-1]
                result = max ( result, h*w)
            stack.append(i)
        return result

print Solution().largestRectangleArea([1])