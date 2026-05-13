class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1, 1:1}

        def f(x):
            if x in memo:
                return memo[x]

            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        
        return f(n)
