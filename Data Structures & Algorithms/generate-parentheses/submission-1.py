class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN, closeN, cur):
            if openN == n and closeN == n:
                res.append("".join(cur))
                return
            if openN < n:
                cur.append("(")
                backtrack(openN + 1, closeN, cur)
                cur.pop()
            if closeN < openN:
                cur.append(")")
                backtrack(openN, closeN + 1, cur)
                cur.pop()
        backtrack(0, 0, [])
        return res