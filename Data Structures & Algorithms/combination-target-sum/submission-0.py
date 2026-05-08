class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, kalan_hedef):
            if kalan_hedef == 0:
                res.append(path.copy())
                return
            
            if kalan_hedef < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                
                backtrack(i, kalan_hedef - nums[i])
                
                path.pop()
        
        backtrack(0, target)
        return res