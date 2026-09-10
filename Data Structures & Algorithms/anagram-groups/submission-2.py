class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}

        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord("a")] += 1
            key = tuple(char)
            if key not in anaMap:
                anaMap[key] = []
            anaMap[key].append(s)
        return list(anaMap.values())