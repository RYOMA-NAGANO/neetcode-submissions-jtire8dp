class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        subDict = {}
        for r in range(len(s)):
            while s[r] in subDict:
                subDict.pop(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            subDict[s[r]] = 1
        return longest

            