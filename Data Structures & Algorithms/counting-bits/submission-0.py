class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            ress = 0
            comp = i
            while comp:
                comp &= (comp - 1)
                ress += 1
            res[i] = ress
        return res