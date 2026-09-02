class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        sorted_queries = []
        for i, q in enumerate(queries):
            sorted_queries.append((q, i))
        sorted_queries.sort()
        minHeap = []
        res = [-1] * len(queries)
        i = 0
        for q, index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            if minHeap:
                res[index] = minHeap[0][0]
        return res