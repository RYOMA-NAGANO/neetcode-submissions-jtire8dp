class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        stairs = [0, 1]
        i = 1
        while i <= n:
            if n >= 1:
                temp = stairs[1]
                stairs[1] = stairs[0] + stairs[1]
                stairs[0] = temp
                i += 1 
        return stairs[1]