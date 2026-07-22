# [1, 4], [4, 5], [6, 7] -> [1, 5], [6, 7]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start > prev_end: # safe as own interval
                res.append([start, end])
                prev_end = end
            else:
                prev_end = max(prev_end, end)
                res[-1][1] = prev_end
        return res