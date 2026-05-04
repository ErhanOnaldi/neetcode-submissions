class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = minPrice if minPrice < price else price
            isProfit = price - minPrice
            maxProfit = maxProfit if maxProfit > isProfit else isProfit
        return maxProfit
  
        