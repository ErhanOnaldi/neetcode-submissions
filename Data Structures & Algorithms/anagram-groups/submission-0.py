class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        result = []
        for s in strs:
            sort = sorted(s)
            res[str(sort)].append(s)
    
        for k,v in res.items():
            result.append(v)
        
        return result
