class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        if end == 0:
            return True
        maxRange = 0
        for i in range(len(nums) - 1):
            jumpRange = i + nums[i]    
            maxRange = max(jumpRange, maxRange)
            if maxRange < i + 1:
                return False
            if maxRange >= end:
                return True
        
        return False
        

