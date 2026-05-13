class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = cur 
        return pre1 
