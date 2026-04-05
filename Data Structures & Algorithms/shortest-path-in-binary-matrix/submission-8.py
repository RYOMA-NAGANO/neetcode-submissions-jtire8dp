class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0)])
        visit = {(0, 0)}
        length = 1
        neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0],
                     [-1, -1], [-1, 1], [1, -1], [1, 1]]

        while q:
            for _ in range(len(q)):                     # one BFS layer
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    visit.add((nr, nc))                 # mark before enqueue
                    q.append((nr, nc))
            length += 1                                 # increment per layer

        return -1