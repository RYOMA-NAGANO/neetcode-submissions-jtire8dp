class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        res, fresh = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        def checkLayer(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0 or grid[r][c] == 2):
                return
            grid[r][c] = 2
            fresh -= 1
            q.append([r, c])
            visited.add((r, c))
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                checkLayer(r + 1, c)
                checkLayer(r - 1, c)
                checkLayer(r, c + 1)
                checkLayer(r, c - 1)
            res += 1
        return res if not fresh else -1