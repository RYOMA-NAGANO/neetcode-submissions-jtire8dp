class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            else:
                if stack:
                    p = stack.pop()
                    if (p == "[" and s[i] != "]") or (p == "{" and s[i] != "}") or (p == "(" and s[i] != ")"):
                        return False
                else:
                    return False
        return stack == []