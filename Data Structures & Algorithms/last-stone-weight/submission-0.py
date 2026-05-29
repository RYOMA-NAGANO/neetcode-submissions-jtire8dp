class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            weight1 = stones.pop()
            weight2 = stones.pop()
            stones.append(abs(weight1 - weight2))
        return stones[-1]