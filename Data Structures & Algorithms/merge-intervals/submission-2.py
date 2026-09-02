class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                start = res[-1][0]
                end = max(end, res[-1][1])
                res.pop()
                res.append([start, end])
        return res