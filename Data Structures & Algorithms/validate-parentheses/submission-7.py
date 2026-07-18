class Solution:
    def isValid(self, s: str) -> bool:
        stringDict = {"[": "]", "{": "}", "(": ")"}
        res = []
        for i in range(len(s)):
            if s[i] in ["{", "(", "["]:
                res.append(s[i])
                continue
            if res == []: return False
            left = res.pop()
            if s[i] != stringDict[left]:
                return False
        return True if res == [] else False
            