from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list) # key -> [(timestamp, val), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.cache[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            timestamp_prev = self.cache[key][mid][0]
            if timestamp_prev > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if right == -1:
            return ''
        return self.cache[key][right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)