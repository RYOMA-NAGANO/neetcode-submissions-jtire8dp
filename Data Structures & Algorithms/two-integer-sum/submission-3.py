class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        graph = {}
        for i in range(len(nums)):
            if target - nums[i] in graph:
                return [graph[target - nums[i]], i]
            else:
                graph[nums[i]] = i
