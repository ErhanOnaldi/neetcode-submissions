class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        visited = set()
        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return 

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                backtrack()
                path.pop()
                visited.remove(nums[i])
        
        backtrack()
        return res