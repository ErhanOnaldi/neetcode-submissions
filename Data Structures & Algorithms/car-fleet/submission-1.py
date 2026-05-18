class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk = []
        for pos,spd in cars:
            time = (target - pos) / spd
            if not stk:
                stk.append(time)
            else:
                if not stk[-1] >= time:
                    stk.append(time)
                    
            
        return len(stk)
                
                
