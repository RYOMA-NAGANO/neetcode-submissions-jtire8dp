class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curList, totalList = [], []
        def helper(i, nums, curList, totalList):
            if i >= len(nums):
                totalList.append(curList.copy())
                return
            
            curList.append(nums[i])
            helper(i + 1, nums, curList, totalList)
            curList.pop()

            helper(i + 1, nums, curList, totalList)
        helper(0, nums, curList, totalList)
        return totalList