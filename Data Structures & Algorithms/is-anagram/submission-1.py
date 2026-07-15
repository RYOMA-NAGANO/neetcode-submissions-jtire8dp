class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        anagram = {}
        for i in range(n):
            if s[i] in anagram:
                anagram[s[i]] += 1
            else:
                anagram[s[i]] = 1
        for j in range(n):
            if t[j] not in anagram or anagram[t[j]] == 0:
                return False
            anagram[t[j]] -= 1
        return True