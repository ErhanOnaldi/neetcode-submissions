from collections import Counter 
class Solution: 
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums)
        res = []
        for k,v in c.items():
            if v > n/3:
                res.append(k)
        
        return res