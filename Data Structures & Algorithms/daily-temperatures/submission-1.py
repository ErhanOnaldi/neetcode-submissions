class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        monotonicStack = []

        for dI, dT in enumerate(temperatures):

            while monotonicStack and dT > temperatures[monotonicStack[-1]]:
                prevDay = monotonicStack.pop()
                res[prevDay] = dI - prevDay

            monotonicStack.append(dI) 

        return res   