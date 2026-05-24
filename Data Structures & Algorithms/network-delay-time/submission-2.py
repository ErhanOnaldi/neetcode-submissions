import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = {}
        heap = [(0,k)]

        while heap:
            d, node = heapq.heappop(heap)

            if node in dist:
                continue
            
            dist[node] = d

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap,(d + weight,nei))

        max_time = 0

        for t in dist.values():
            max_time = max(t,max_time)
    
        return max_time if len(dist) == n else -1
            