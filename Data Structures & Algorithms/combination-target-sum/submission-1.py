class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start,target):
            if target == 0:
                res.append(path.copy())
    
            if target < 0:
                return
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,target - nums[i])
                path.pop()


        backtrack(0,target)
        return res