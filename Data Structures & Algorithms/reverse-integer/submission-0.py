class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        limit = 2**31 - 1 if sign == 1 else 2**31

        while x:
            digit = x % 10
            x //= 10

            if res > (limit - digit) // 10:
                return 0
            
            res = res * 10 + digit
        return res * sign