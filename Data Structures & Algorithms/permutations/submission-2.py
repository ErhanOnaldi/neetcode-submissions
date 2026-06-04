class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        visited = set()
        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                dfs()
                path.pop()
                visited.remove(nums[i])

        dfs()
        return res