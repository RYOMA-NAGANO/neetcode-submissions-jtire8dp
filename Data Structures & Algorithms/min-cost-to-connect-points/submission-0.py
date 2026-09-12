class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        graph = {i : [] for i in range(n)}

        for i in range(n):
            x1, x2 = points[i]
            for j in range(i + 1, n):
                y1, y2 = points[j]
                distance = abs(x1 - y1) + abs(x2 - y2)

                graph[i].append((distance, j))
                graph[j].append((distance, i))

        minHeap = [(0, 0)]
        res = 0
        visited = set()

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += cost

            for neiCost, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))

        return res