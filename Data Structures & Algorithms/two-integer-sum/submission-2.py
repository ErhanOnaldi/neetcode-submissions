class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx,num in enumerate(nums): #O(N)
            seen[num] = idx


        for idx in range(len(nums)): #O(N)
            candidate = target - nums[idx]
            if candidate in seen: #O(1)
                if idx != seen[candidate]:
                    return [idx, seen[candidate]]
            
    
        return []

            