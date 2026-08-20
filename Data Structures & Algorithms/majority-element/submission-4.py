class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = 0
        n = 0
        for k,v in c.items():
            if v > m:
                m = v 
                n = k

        return n