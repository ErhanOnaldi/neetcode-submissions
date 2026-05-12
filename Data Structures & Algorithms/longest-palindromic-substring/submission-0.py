class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while (
                l >= 0 and
                r < len(s) and
                s[l] == s[r]
            ):
                l -= 1
                r += 1

            return s[l+1:r]

        for i in range(len(s)):

            p1 = expand(i, i)

            p2 = expand(i, i+1)

            longer = p1 if len(p1) > len(p2) else p2

            if len(longer) > len(res):
                res = longer

        return res