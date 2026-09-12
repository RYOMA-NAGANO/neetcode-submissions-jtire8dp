class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([beginWord])
        visited = {beginWord}

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:j] + c + word[j + 1 : ]

                        if (newWord in wordSet and newWord not in visited):
                            visited.add(newWord)
                            q.append(newWord)
            res += 1
        return 0