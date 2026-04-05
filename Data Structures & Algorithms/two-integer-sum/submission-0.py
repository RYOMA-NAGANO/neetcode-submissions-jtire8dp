class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        res = [0] * 2
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                if hashmap[target - nums[i]] > i:
                    res[0] = i
                    res[1] = hashmap[target - nums[i]]
                else:
                    res[0] = hashmap[target - nums[i]]
                    res[1] = i
            else:
                hashmap[nums[i]] = i
        return res