class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        targetsum = 0
        def dfs(i, target):
            nonlocal targetsum
            if i >= len(nums):
                return
            if targetsum > target:
                return
            if targetsum == target:
                res.append(subset.copy())
                return
            targetsum += nums[i]
            subset.append(nums[i])
            dfs(i, target)
            targetsum -= nums[i]
            subset.pop()
            dfs(i + 1, target)
        dfs(0, target)
        return res
            
