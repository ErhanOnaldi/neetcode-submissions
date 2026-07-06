class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            if op == "+":
                o1= s[-1]
                o2 = s[-2]
                s.append(o1 + o2)
            elif op == "D":
                s.append(s[-1] * 2)
            elif op == "C":
                s.pop()
            else:
                s.append(int(op))
        
        return sum(s)
