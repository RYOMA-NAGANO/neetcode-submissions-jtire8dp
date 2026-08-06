class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.data)):
            if key == self.data[i][0]:
                self.data[i][1] = value
                return
        self.data.append([key, value])

    def get(self, key: int) -> int:
        for i in range(len(self.data)):
            if key == self.data[i][0]:
                return self.data[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.data)):
            if key == self.data[i][0]:
                self.data.remove(self.data[i])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)