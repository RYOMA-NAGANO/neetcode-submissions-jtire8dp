class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occ = set()
        for num in nums:
            if num not in occ:
                occ.add(num)
            else:
                occ.remove(num)
        
        for x in occ:
            return x