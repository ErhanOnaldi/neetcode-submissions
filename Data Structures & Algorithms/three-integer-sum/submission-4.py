class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for candidateIndex in range(n):
            l = candidateIndex + 1
            if candidateIndex > 0 and nums[candidateIndex] == nums[candidateIndex - 1]:
                continue
            r = n - 1 
            while l < r:
                s = nums[candidateIndex] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[candidateIndex], nums[l], nums[r]])
                    r -= 1
                    l += 1 
                    while l < r and nums[l] == nums[l - 1]:

                        l += 1

                    while l < r and nums[r] == nums[r + 1]:

                        r -= 1
                elif s > 0:
                    r -=1
                else:
                    l += 1
        
        return res