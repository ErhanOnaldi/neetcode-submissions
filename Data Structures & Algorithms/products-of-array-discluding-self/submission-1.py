class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        mult = 1
        for i in range(n):
            prefix[i] = mult
            mult *= nums[i]

        mult = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = mult
            mult *= nums[i]

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]

        return nums