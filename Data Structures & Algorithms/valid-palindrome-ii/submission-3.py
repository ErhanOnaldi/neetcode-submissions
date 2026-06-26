class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        r = n - 1
        l = 0
        already_deleted = [False]

        def palindrome(l,r):
            if l >= r:
                return True
            if s[l] != s[r]:
                if already_deleted[0]:
                    return False
                else:
                    already_deleted[0] = True
                    return palindrome(l + 1, r) or palindrome(l, r - 1)

            return palindrome(l + 1, r - 1 )
             
        return palindrome(l,r)
            
            