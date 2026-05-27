class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        targetsum = 0
        candidates.sort()
        def dfs(i, target):
            nonlocal targetsum
            if targetsum == target:
                res.append(subset.copy())
                return
            if i >= len(candidates):
                return
            if targetsum > target:
                return
            targetsum += candidates[i]
            subset.append(candidates[i])
            dfs(i + 1, target)
            targetsum -= candidates[i]
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, target)
        dfs(0, target)
        return res
            