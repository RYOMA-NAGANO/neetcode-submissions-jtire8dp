class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1), len(word2))

            if (len(word1) > len(word2) and word1[: minLen] == word2[: minLen]):
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        visited = set()
        visiting = set()
        res = []
        def dfs(c):
            if c in visited:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for nei in graph[c]:
                if not dfs(nei):
                    return False
            visited.add(c)
            res.append(c)
            visiting.remove(c)
            return True
        for char in graph:
            if not dfs(char):
                return ""
        return "". join(res[::-1])