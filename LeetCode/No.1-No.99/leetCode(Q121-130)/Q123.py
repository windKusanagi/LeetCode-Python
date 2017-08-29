class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        prices = [2, 4, 6, 1, 3, 8, 3]
        """
        minPrice, MaxProfit = 2**16-1, 0
        firstStock = [0 for __ in range(len(prices))]
        result = 0
        for i in range(len(prices)):
            minPrice = min (prices[i] , minPrice)
            MaxProfit = max(MaxProfit, prices[i] - minPrice)
            firstStock[i] = MaxProfit
        maxPrice, curMaxProfit = 0 , 0
        for i in range(len(prices)-1, 0, -1):
            maxPrice = max (maxPrice, prices[i])
            curMaxProfit = max(curMaxProfit , maxPrice-prices[i])
            MaxProfit = max( MaxProfit, curMaxProfit + firstStock[i-1])

        return MaxProfit

if __name__ == "__main__":
    print Solution().maxProfit([2, 4, 6, 1, 3, 8, 3])
    print Solution().maxProfit([1, 2])
