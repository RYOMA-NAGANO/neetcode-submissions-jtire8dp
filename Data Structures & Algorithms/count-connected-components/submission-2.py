class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i : [] for i in range(n)}

        for pre, post in edges:
            preMap[pre].append(post)
            preMap[post].append(pre)
        visited = set()
        res = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in preMap[node]:
                dfs(nei)
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        return res