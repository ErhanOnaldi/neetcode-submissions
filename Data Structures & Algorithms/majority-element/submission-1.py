class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityNum = float("inf")
        ct = 1

        for num in nums:
            if majorityNum == num:
                ct += 1
            else:
                ct -= 1
                if ct <= 0:
                    majorityNum = num
                    ct += 1
        
        return majorityNum
