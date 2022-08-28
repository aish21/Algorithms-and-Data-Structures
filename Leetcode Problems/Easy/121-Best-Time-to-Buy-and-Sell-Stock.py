class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for p in prices[1:]:
            if p < minPrice:
                minPrice = p
            elif maxProfit < p - minPrice:
                maxProfit = p - minPrice
        return maxProfit
        