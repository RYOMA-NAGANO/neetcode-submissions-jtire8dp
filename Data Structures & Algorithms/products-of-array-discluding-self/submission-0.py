class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            pre = nums[0 : i]
            suffix = nums[i + 1 : len(nums)]
            res, j = 1, 0
            while j < len(pre) or j < len(suffix):
                if j < len(pre):
                    res *= pre[j]
                if j < len(suffix):
                    res *= suffix[j]
                j += 1             
            output.append(res)
        return output

