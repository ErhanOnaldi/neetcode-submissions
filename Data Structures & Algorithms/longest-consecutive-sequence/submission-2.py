class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                length = 1
                curr = num
                while curr + 1 in s:
                    curr += 1
                    length += 1
                longest = max(longest, length)

        return longest