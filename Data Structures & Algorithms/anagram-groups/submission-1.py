class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagram = {}
        for s in strs:
            char = [0] * 26
            for c in s:
                char[ord(c) - ord("a")] += 1
            key = tuple(char)
            if key not in groupAnagram:
                groupAnagram[key] = []

            groupAnagram[key].append(s)
        return list(groupAnagram.values())