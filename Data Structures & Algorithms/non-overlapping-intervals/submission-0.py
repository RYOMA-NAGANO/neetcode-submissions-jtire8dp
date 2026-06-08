class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        copy = []
        for start, end in intervals:
            if not copy or start >= copy[-1][1]:
                copy.append([start, end])
            else:
                copy[-1] = [min(copy[-1][0], start), min(copy[-1][1], end)]
                res += 1
        return res