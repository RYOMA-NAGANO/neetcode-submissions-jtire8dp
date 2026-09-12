class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        graph = {}
        for num in nums:
            if num in graph:
                return True
            else:
                graph[num] = 1
        return False