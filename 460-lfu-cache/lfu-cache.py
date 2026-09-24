from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> val
        self.freq = {} # key -> frequency
        self.buckets = defaultdict(OrderedDict) # freq -> keys
        self.min_freq = 0

    def _bump(self, key):
        f = self.freq[key]
        del self.buckets[f][key]
        if not self.buckets[f]:
            del self.buckets[f]
            if self.min_freq == f:
                self.min_freq += 1

        self.freq[key] += 1
        self.buckets[f + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._bump(key)
        return self.cache[key]        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self._bump(key)
            return

        if len(self.cache) == self.capacity:
            evict, _ = self.buckets[self.min_freq].popitem(last=False)
            del self.cache[evict], self.freq[evict]

        self.cache[key] = value
        self.freq[key] = 1
        self.min_freq = 1
        self.buckets[1][key] = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)