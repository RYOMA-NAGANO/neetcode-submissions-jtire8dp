class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ""
        for i in range(len(s)):
            if not (ord("a") <= ord(s[i]) <= ord("z") or ord("A") <= ord(s[i]) <= ord("Z") or ord("0") <= ord(s[i]) <= ord("9")):
                continue
            else:
                cleaned_text += s[i]
        l, r = 0, len(cleaned_text) - 1
        while l < r:
            if cleaned_text[l].lower() != cleaned_text[r].lower():
                return False
            l += 1
            r -= 1

        return True