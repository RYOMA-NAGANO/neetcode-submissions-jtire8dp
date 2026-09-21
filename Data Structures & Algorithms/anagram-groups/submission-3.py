class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord("a")] += 1

            anagramMap[tuple(char)].append(s)
        return list(anagramMap.values())