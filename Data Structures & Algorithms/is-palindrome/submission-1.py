class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        L = 0
        R = len(filtered) - 1
        while L < R:
            if filtered[L] != filtered[R]:
                return False
            L+=1
            R-=1
        
        return True