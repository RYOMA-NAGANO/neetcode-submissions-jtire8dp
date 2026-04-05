class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = dict()
        for i in range(len(nums)):
            if nums[i] in duplicate:
                return nums[i]
            else:
                duplicate[nums[i]] =1