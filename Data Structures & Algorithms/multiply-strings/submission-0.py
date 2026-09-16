class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        total = 0
        occ = 0
        for i in range(len(num2) - 1, -1, -1):
            if occ == 0:
                total += (int(num1) * int(num2[i]))
            else:
                total += (int(num1) * int(num2[i]) * (10**occ))
            
            occ += 1
        return str(total)
