class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeenDict = {}
        res = []
        for i in range(len(s)):
            if s[i] not in lastSeenDict:
                lastSeenDict[s[i]] = i
            else:
               lastSeenDict[s[i]] = max(i,lastSeenDict[s[i]]) 
        maxRange = 0
        start = float("inf")
        for i in range(len(s)):
            start = min(start,i)
            maxRange = max(maxRange,lastSeenDict[s[i]])
            if i == maxRange:
                res.append(maxRange - start + 1)
                start = float("inf")

        return res

            
