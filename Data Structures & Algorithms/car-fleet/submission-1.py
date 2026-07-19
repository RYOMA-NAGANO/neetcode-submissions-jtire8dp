class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        res= []
        for i in range(len(pairs)):
            time = (target - pairs[i][0]) / pairs[i][1]
            if not res:
                res.append(time)
            elif time > res[-1]:
                res.append(time)
        return len(res)