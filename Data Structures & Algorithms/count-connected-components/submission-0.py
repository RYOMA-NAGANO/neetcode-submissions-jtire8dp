class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i: [] for i in range(n)}
        visiting = set()
        for pre, succ in edges:
            preMap[pre].append(succ)
            preMap[succ].append(pre)
        res = 0
        def dfs(node):
            if node in visiting:
                return
            visiting.add(node)
            for nei in preMap[node]:
                dfs(nei)
        for node in range(n):
            if node not in visiting:
                res += 1
                dfs(node)
        return res    