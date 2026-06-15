class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct = 0
        for idx,num in enumerate(nums):
            if num == val:
                nums[idx] = -1
            else:
                ct += 1
                
        nums.sort(reverse = True)
        return ct
            