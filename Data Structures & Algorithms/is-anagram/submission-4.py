class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sSet = Counter(s)
        tSet = Counter(t)

        return sSet == tSet