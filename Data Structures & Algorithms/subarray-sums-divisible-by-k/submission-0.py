class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix, count = 0, 0
        freq = {0 : 1}
        for num in nums:
            prefix += num
            remain = prefix % k
            count += freq.get(remain, 0)
            freq[remain] = freq.get(remain, 0) + 1
        return count