class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {0:nums[0], 1: max(nums[0],nums[1]) }

        def f(x):
            if x in memo:
                return memo[x]
            
            memo[x] = max(f(x-1), nums[x] + f(x - 2))
            return memo[x]

        return f(len(nums) - 1)