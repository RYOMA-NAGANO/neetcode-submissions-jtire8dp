class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < tail and not self.isAlphaNum(s[head]):
                head += 1
            while tail > head and not self.isAlphaNum(s[tail]):
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
    def isAlphaNum(self, c):
        return (ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9") or ord("A") <= ord(c) <= ord("Z")) 
        