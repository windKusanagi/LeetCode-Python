class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        result = 0
        length = len(height)
        maxheightR = [ 0 for __ in range(length)]
        temp = height[length-1]
        for i in range( length -2 , -1 , -1):
            maxheightR[i] = temp
            temp = max(maxheightR[i],height[i])

        temp1 = height[0]
        for i in range (1, length -1):
            temp1 = max (temp1, height[i])
            result += max (min(temp1, maxheightR[i]) - height[i] , 0 )

        return result
print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])