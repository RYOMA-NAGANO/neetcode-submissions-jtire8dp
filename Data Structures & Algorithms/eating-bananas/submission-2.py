class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = 0
        while left <= right:
            total = 0
            middle = (left + right) // 2
            for p in piles:
                total += math.ceil(p / middle)
            if total > h:
                left = middle + 1
            else:
                right = middle - 1
                res = middle
        return res

