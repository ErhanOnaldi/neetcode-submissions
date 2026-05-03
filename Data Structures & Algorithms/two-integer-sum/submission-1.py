class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict ={}
        for i in range(len(nums)):
            numDict[nums[i]] = i 

        for i in range(len(nums)):
            if target - nums[i] in numDict:
                if numDict[target - nums[i]] == i:
                    continue
                if numDict[target - nums[i]] < i:
                    return [numDict[target - nums[i]], i]
                else:
                    return [i,numDict[target - nums[i]]]
        
        return []