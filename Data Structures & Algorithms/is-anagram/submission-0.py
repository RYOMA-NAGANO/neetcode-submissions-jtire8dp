class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = dict()
        tDict = dict()
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        for j in range(len(s)):
            if t[j] in s and tDict[t[j]] == sDict[t[j]]:
                continue
            else:
                return False
        return True
            