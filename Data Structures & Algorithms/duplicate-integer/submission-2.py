class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            else:
                duplicate[nums[i]] = 1
        return False