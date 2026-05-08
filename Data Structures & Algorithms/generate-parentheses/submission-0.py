class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(openP, closedP):
            if openP + closedP == n * 2:
                res.append("".join(path))
                return
            
            if openP < n:
                path.append("(")             # SEÇ
                backtrack(openP + 1, closedP) # SORGULA (Açık sayısını 1 artırarak derine in)
                path.pop()                   # VAZGEÇ (Sil)

            if closedP < openP:
                path.append(")")             # SEÇ
                backtrack(openP, closedP + 1) # SORGULA (Kapalı sayısını 1 artırarak derine in)
                path.pop()                   # VAZGEÇ (Sil)
                
        backtrack(0, 0) 
        return res