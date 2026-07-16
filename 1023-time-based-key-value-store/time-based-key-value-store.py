class TimeMap:

    def __init__(self):
        # key -> [(timestamp, value)]
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        left, right = 0, len(self.store[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            prev_time = self.store[key][mid][0]
            if prev_time > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return '' if right < 0 else self.store[key][right][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)