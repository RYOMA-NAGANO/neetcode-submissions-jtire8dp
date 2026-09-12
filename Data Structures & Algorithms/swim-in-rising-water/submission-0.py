class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return time
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited):
                    continue
                newTime = max(time, grid[nr][nc])
                heapq.heappush(minHeap, (newTime, nr, nc))
        return time
            