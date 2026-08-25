class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curList, totalList = [], []
        def isPanlidrom(res):
            l, r = 0, len(res) - 1
            while l < r:
                if res[l] != res[r]:
                    return False
                l += 1
                r -= 1
            return True

        def helper(i, s, curList, totalList):
            if i == len(s):
                totalList.append(curList.copy())
                return
            for j in range(i, len(s)):
                res = s[i:j + 1]
                if isPanlidrom(res):
                    curList.append(res)
                    helper(j + 1, s, curList, totalList)
                    curList.pop()

        helper(0, s, curList, totalList)
        return totalList