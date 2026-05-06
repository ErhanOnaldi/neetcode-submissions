import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)   

        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)
            smash = num1 - num2
            if smash != 0:
                heapq.heappush(heap,smash)
    
        return abs(heap[0]) if len(heap) == 1 else 0 