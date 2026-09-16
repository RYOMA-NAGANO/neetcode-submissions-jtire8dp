class CountSquares:

    def __init__(self):
        self.counts = {}
        self.points = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] = self.counts.get((x, y), 0) + 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px, py in self.points:
            if abs(px - x) != abs(py - y):
                continue
            
            if x == px or y == py:
                continue

            res += (self.counts.get((px, y), 0) * self.counts.get((x, py), 0))
        return res