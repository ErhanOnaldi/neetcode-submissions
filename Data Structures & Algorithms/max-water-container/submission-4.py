class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[r],heights[l])
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -=1
            else:
                l += 1
                r -=1
    
        return maxArea
