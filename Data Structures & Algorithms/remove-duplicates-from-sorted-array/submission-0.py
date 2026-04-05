class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[k]:
                k += 1
                nums[k] = nums[i + 1]
        return k + 1    