class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hset = {}
        for num in arr:
            hset[num] = hset.get(num, 0) + 1
        ans = 0
        for num, freq in hset.items():
            if num > ans and num == freq:
                ans = num
        if ans == 0:
            return -1
        else:
            return ans