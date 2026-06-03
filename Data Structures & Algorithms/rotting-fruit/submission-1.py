class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res, fresh = 0, 0
        rotten = deque()
        def checkLayer(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 2 or grid[r][c] == 0):
                return
            if grid[r][c] == 1:
                fresh -= 1
                grid[r][c] = 2
                rotten.append([r, c])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r, c])
        while rotten and fresh:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                checkLayer(r + 1, c)
                checkLayer(r - 1, c)
                checkLayer(r, c - 1)
                checkLayer(r, c + 1)
            res += 1
        return res if not fresh else -1
                