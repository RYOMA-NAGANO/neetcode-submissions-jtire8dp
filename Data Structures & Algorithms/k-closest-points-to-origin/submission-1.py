class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i, (x, y) in enumerate(points):
            res.append([x * x + y * y, i])
        heapq.heapify(res)
        ans = []
        for i in range(k):
            distance, i = heapq.heappop(res)
            ans.append(points[i])
        return ans
        