class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        ret = []
        
        for s in strs:
            sort = sorted(s)
            res[str(sort)].append(s)
        
        for k,v in res.items():
            ret.append(v)

        return ret