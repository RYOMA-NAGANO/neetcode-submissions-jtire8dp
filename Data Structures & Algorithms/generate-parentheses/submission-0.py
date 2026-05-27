class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openP, closeP, res, n, parenthesis):
            if len(parenthesis) == 2 * n:
                res.append(parenthesis)
                return
            if openP < n:
                dfs(openP + 1, closeP, res, n, parenthesis + "(")
            if closeP < openP:
                dfs(openP, closeP + 1, res, n, parenthesis + ")")   
        dfs(0, 0, res, n, "")              
        return res