class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n + 1)}

        for src, target, distance in times:
            graph[src].append([target, distance])

        res = 0
        minHeap = [(0, k)]
        visited = set()
        while minHeap:
            distance, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)

            res = max(res, distance)

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (distance + weight, nei))
        
        if len(visited) == n:
            return res
        return -1