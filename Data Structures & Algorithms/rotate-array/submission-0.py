class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0
        while count < n:
            current = start
            previous = nums[current]
            while True:
                next_index = (current + k) % n 
                nums[next_index], previous = previous, nums[next_index]

                current = next_index
                count += 1
                if current == start:
                    break
            start += 1
        
