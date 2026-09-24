import random
class RandomizedSet:

    def __init__(self):
        self.cache = {} # val -> idx
        self.arr = [] # val

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        self.arr.append(val)
        self.cache[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        idx = self.cache[val]
        last = self.arr[-1]
        self.cache[last] = idx
        self.arr[idx] = last

        self.arr.pop()
        del self.cache[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()