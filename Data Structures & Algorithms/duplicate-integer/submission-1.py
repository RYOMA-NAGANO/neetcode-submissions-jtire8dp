class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = dict()
        for i in range(n):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False