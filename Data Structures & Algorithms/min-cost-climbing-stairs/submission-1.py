class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1: 0}
        def f(x):
            if x in memo:
                return memo[x]

            memo[x] =  min(cost[x - 1] + f(x - 1),cost[x - 2] + f(x - 2))
            return memo[x]

        return f(len(cost))
