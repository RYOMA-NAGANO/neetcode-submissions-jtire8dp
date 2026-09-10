class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        occ = []
        for num, cnt in freq.items():
            occ.append([cnt, num])
        occ.sort()

        res = []
        for i in range(len(occ) - 1, len(occ) - 1 - k, -1):
            res.append(occ[i][1])
        return res