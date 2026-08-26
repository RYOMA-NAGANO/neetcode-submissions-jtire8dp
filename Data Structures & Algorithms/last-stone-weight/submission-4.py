class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            operand1 = heapq.heappop(stones)
            operand2 = heapq.heappop(stones)
            res = operand1 - operand2
            heapq.heappush(stones, res)
        return -stones[0]