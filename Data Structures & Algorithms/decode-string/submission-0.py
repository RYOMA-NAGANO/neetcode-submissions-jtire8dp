class Solution:
    def decodeString(self, s: str) -> str:
        decode = []
        curStr = ""
        curNum = 0
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c == "[":
                decode.append((curStr, curNum))
                curStr = ""
                curNum = 0
            elif c == "]":
                prev, num = decode.pop()
                curStr = prev + curStr * num
            else:
                curStr += c
        return curStr