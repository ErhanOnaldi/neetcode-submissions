class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for k in sorted(counter.keys()):
            count = counter[k]  
            
            if count > 0:
                for i in range(groupSize):
                    nextCard = k + i
                    if counter[nextCard] < count:
                        return False                        
                    counter[nextCard] -= count

        return True