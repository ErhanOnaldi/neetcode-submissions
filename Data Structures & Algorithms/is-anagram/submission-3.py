class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = Counter(s)
        tSet = Counter(t)

        return sSet == tSet