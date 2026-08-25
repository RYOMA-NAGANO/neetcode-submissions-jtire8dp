class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curList, totalList = [], []
        curNum = 0
        def helper(i, curNum, curList, totalList, target):
            if curNum == target:
                totalList.append(curList.copy())
                return
            if i >= len(candidates) or curNum > target:
                return
            curList.append(candidates[i])
            helper(i + 1, curNum + candidates[i], curList, totalList, target)
            curList.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, curNum, curList, totalList, target)
        candidates.sort()
        helper(0, curNum, curList, totalList, target)
        return totalList
            
                
            