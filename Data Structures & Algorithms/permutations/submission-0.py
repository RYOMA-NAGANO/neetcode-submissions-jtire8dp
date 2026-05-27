class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def backtrack(nums, subset, pick, res):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    backtrack(nums, subset, pick, res)
                    subset.pop()
                    pick[i] = False
        backtrack(nums, [], pick, res)   
        return res