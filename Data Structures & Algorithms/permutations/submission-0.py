class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking():
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for i in nums:
                if i in path:
                    continue 
                path.append(i)
                backtracking()
                path.pop()

        backtracking() 
        return res