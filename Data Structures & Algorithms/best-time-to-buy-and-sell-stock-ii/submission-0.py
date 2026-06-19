class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum_profit = 0
        stock = prices[0]
        for price in prices:
            profit = price - stock
            if profit >= 1:
                sum_profit += profit
            
            stock = price
        
        return sum_profit
            