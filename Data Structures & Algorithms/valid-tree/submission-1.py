class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        preMap = {i: [] for i in range(n)}

        for parent, child in edges:
            preMap[parent].append(child)
            preMap[child].append(parent)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for neighbor in preMap[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
            