class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curList, totalList = [], []
        def helper(i, nums, target, curList, totalList):
            if i >= len(nums):
                return
            if target == 0:
                totalList.append(curList.copy())
                return
            if target > 0:
                curList.append(nums[i])
                helper(i, nums, target - nums[i], curList, totalList)
                curList.pop()
            helper(i + 1, nums, target, curList, totalList)
        helper(0, nums, target, curList, totalList)
        return totalList


