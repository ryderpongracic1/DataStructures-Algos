class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        res = 0

        prev_end = intervals[0][1] # earliest ending interval
        for start, end in intervals[1:]:
            # curr interval starts before prev interval ends
            if start < prev_end:
                # remove curr
                res += 1
            else:
                # curr is save & used, update prev_end
                prev_end = end
        return res