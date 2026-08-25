class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curList, totalList = [], []
        def helper(i, nums, curList, totalList):
            if i >= len(nums):
                totalList.append(curList.copy())
                return
            curList.append(nums[i])
            helper(i + 1, nums, curList, totalList)
            curList.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, curList, totalList)
        nums.sort()
        helper(0, nums, curList, totalList)
        return totalList