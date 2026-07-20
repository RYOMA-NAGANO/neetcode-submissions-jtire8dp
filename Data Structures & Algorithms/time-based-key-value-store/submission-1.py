class TimeMap:

    def __init__(self):
        self.timeStampDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStampDict:
            self.timeStampDict[key] = []
        self.timeStampDict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.timeStampDict.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= values[mid][1]:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
