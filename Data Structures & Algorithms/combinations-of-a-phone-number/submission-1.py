class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneDict = {"2" : "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        curList, totalList = [], []
        def helper(i, digits, curList, totalList):
            if i == len(digits):
                totalList.append("".join(curList.copy()))
                return
            phoneList = phoneDict[digits[i]]
            for s in phoneList:
                curList.append(s)
                helper(i + 1, digits, curList, totalList)
                curList.pop()
                
        helper(0, digits, curList, totalList)
        return totalList