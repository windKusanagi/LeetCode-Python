class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        low , high = prices[0], prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>high:
                high = prices[i]
            else:
                profit += high - low
                low, high = prices[i] , prices[i]
        profit += high - low
        return profit
print Solution().maxProfit([3,1,2])
print Solution().maxProfit([3, 1, 1, 4, 2, 5, 6, 3, 2, 1, 4, 2, 5, 6])