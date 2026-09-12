class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}

        for start, dest, cost in flights:
            graph[start].append([dest, cost])
        
        minHeap = [(0, src, 0)]
        best = [[float("inf")] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while minHeap:
            distance, node, step = heapq.heappop(minHeap)    
            if node == dst:
                return distance
            if step == k + 1:
                continue
            if distance > best[node][step]:
                continue
            for nei, neiCost in graph[node]:
                newDistance = distance + neiCost
                newSteps = step + 1
                if newDistance < best[nei][newSteps]:
                    best[nei][newSteps] = newDistance
                heapq.heappush(minHeap, (newDistance, nei, newSteps))
        return -1