class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurrence = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[occurrence] = nums[i]
                occurrence += 1
        return occurrence
