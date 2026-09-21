class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrence = {}
        for num in nums:
            occurrence[num] = occurrence.get(num, 0) + 1
        sorted_map = dict(sorted(occurrence.items(), key = lambda x: x[1]))
        return list(sorted_map)[::-1][:k]