class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        total = 0
        ct = 0
        for num in nums:
            total += num
            if total == k:
                ct += 1
            if (total - k) in d:
                ct += d[total - k]

            d[total] += 1

        return ct    
