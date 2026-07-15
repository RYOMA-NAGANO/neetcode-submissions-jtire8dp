class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in twoSum:
                return [twoSum[target - nums[i]], i]
            else:
                twoSum[nums[i]] = i
        