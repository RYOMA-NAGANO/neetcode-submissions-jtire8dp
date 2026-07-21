class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        res = ""
        l = 0
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        needCount = len(need)
        window = {}
        have = 0
        resLen = float("inf")
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and need[s[r]] == window[s[r]]:
                have += 1
            while have == needCount:
                if r - l + 1 < resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res