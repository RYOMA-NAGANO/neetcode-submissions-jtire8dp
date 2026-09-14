class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_array = [0] * n
        min_array = [0] * n

        max_array[0] = nums[0]
        min_array[0] = nums[0]

        res = nums[0]
        for i in range(1, n):
            cur = nums[i]

            max_array[i] = max(cur, max_array[i - 1] * cur, min_array[i - 1] * cur)
            min_array[i] = min(cur, max_array[i - 1] * cur, min_array[i - 1] * cur)

            res = max(res, max_array[i])
        return res