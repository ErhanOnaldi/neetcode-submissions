class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = defaultdict(int)
        for i in nums:
            visited[i] = 0
        maxCount = 0
        for j in nums:
            if visited[j] == 1:
                continue
            count = 1
            i = j
            visited[i] = 1
            while i+1 in visited:
                count += 1
                visited[i + 1] = 1
                i += 1
            maxCount = max(count,maxCount)

        return maxCount
            