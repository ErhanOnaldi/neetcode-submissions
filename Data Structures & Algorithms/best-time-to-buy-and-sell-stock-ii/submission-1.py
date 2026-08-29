class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float("inf")
        for price in prices:
            min_so_far = min(min_so_far,price)
            is_profit = price - min_so_far
            if is_profit > 0:
                max_profit += is_profit
                min_so_far = price

        
        return int(max_profit)