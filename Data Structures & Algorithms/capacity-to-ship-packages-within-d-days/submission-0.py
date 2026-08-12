class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = 0
        while left <= right:
            total = 1
            curSum = 0
            mid = (left + right) // 2
            for weight in weights:
                if curSum + weight > mid:
                    total += 1
                    curSum = weight
                else:
                    curSum += weight
            if total > days:
                left = mid + 1
            else:
                right = mid - 1
                res = mid
        return res
                    
