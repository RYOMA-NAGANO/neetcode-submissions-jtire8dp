class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        res = 0
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbor:
                    if r + dr >= ROWS or c + dc >= COLS or r + dr < 0 or c + dc < 0 or grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2:
                        continue
                    if grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        queue.append((r + dr, c + dc))
            res += 1
        return res if fresh == 0 else -1