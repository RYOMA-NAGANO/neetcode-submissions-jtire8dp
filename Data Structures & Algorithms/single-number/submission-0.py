class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for i in range(len(nums)):
            if nums[i] in single:
                single.remove(nums[i])
            else:
                single.add(nums[i]) 
        return list(single)[0]                                                                                                                                                                        