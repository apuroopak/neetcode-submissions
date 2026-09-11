class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        runningMax = 0
        profit = 0
        for p in prices:
            profit = p - minPrice
            if profit > runningMax:
                runningMax = profit

            if p < minPrice:
                minPrice = p
        
        return runningMax

            

