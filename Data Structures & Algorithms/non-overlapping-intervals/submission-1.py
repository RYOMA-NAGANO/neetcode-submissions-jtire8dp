class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        stack = []
        for start, end in intervals:
            if not stack:
                stack.append([start, end])
            elif start >= stack[-1][1]:
                start = stack[-1][0]
                stack.pop()
                stack.append([start, end])
            else:
                start = stack[-1][0]
                end = min(stack[-1][1], end)
                stack.pop()
                stack.append([start, end])
                res += 1
        return res
