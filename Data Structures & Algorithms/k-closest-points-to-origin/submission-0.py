class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            dist = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
            res.append([dist, points[i][0], points[i][1]])
        heapq.heapify(res)
        ress = []
        for j in range(k):
            x, y, z = heapq.heappop(res)
            ress.append([y, z])
        return ress
        