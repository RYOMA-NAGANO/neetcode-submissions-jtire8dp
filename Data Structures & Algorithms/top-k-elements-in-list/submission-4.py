class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            freq.append([cnt, num])
        
        freq.sort()
        res = []
        for i in range(len(freq) - 1, len(freq) - 1 - k, -1):
            res.append(freq[i][1])
        return res