import random
class RandomizedSet:

    def __init__(self):
        self.arr = [] # val
        self.map = {} # val -> idx

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.map[last] = idx

        del self.map[val]
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()