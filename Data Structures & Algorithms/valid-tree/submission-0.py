class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        preMap = {i: [] for i in range(n)}
        for root, child in edges:
            preMap[root].append(child)
            preMap[child].append(root)
        visiting = set()
        def dfs(node, parent):
            if node in visiting:
                return False
            visiting.add(node)
            for child in preMap[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            preMap[node] = []
            return True
        return dfs(0, -1) and len(visiting) == n
            