class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, kalan_hedef):
            if kalan_hedef == 0:
                res.append(path.copy())
                return
            if kalan_hedef < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > kalan_hedef:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                
                backtrack(i+1, kalan_hedef - candidates[i])
                
                path.pop()
        
        backtrack(0, target)
        return res