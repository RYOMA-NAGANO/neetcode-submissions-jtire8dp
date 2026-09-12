class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        preMap = {i: [] for i in range(n + 1)}
        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)
            for nei in preMap[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False
        
        for pre, post in edges:
            visited = set()
            if dfs(pre, post, visited):
                return [pre, post]
            preMap[pre].append(post)
            preMap[post].append(pre)
            
