class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        i = 0
        n = len(nums)

        while i < n - 1:
            jumpRange = i + nums[i]
            if jumpRange >= n - 1:
                return jumps + 1
            maxRangeToChoose = 0
            indexToChoose = i
            j = i + 1
            while j <= jumpRange:
                if j + nums[j] > maxRangeToChoose:
                    maxRangeToChoose = j + nums[j]
                    indexToChoose = j
                j += 1

            jumps += 1
            i = indexToChoose

        return jumps