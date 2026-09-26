class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i : [] for i in range(n)}

        for pre, post in edges:
            preMap[pre].append(post)
            preMap[post].append(pre)

        visited = set()
        res = 0
        def dfs(node):
            visited.add(node)

            for nei in preMap[node]:
                if nei not in visited:
                    dfs(nei)
        
        for j in range(n):
            if j not in visited:
                dfs(j)
                res += 1
        return res