class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for n, c in count.items():
            frq[c].append(n)
        res = []
        for i in range(len(frq) - 1, -1, -1):
            for n in frq[i]:
                res.append(n)
                if len(res) == k:
                    return res