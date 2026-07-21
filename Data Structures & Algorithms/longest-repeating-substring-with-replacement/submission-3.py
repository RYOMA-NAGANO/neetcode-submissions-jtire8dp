class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueDict = {}
        l, longest = 0, 0
        for r in range(len(s)):  
            if s[r] not in uniqueDict:
                uniqueDict[s[r]] = 1
            else:
                uniqueDict[s[r]] += 1
            maxFrq = max(uniqueDict.values())
            while r - l + 1 - maxFrq > k:
                uniqueDict[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest