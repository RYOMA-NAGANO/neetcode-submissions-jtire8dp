class Solution:
    def jump(self, nums: List[int]) -> int:
        currentEnd = 0
        farthest = 0
        jump = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                jump += 1
                currentEnd = farthest
        return jump