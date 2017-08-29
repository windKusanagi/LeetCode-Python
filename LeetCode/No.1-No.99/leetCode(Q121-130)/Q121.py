class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
            if prices[i] < minPrice:
                minPrice = prices[i]
        return maxProfit

print Solution().maxProfit([7,6,4,3,1])