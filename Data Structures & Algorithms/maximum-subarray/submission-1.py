class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = float('-inf')
        currSum = 0
        for num in nums:
            currSum += num
            sol = max(currSum,sol)
            if currSum < 0:
                currSum = 0
        
        return sol