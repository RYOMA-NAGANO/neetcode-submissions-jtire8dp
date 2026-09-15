class Solution:
    def isValid(self, s: str) -> bool:
        parent = {"[": "]", "(": ")", "{": "}"}
        stack = []
        for c in s:
            if c in parent:
                stack.append(c)
            else:
                if stack == [] or c != parent[stack.pop()]:
                    return False
                else:
                    continue
        return True if stack == [] else False