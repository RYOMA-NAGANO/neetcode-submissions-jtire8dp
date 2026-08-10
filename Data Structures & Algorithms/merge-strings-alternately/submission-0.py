class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        if len(word1) <= len(word2):
            r = len(word1) - 1
        else:
            r = len(word2) - 1
        res = ""
        while l <= r:
            res += word1[l]
            res += word2[l]
            l += 1
        word1 = word1[l:]
        word2 = word2[l:]
        if word1:
            res += word1
        if word2:
            res += word2
        return res