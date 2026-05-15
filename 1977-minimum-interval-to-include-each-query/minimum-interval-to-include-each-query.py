import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        sorted_q = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)

        min_heap = []
        i = 0
        for query, idx in sorted_q:
            # add all intervals that hae started by this query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1

            # remove small intervals that ended before query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # query found & is the smallest
            if min_heap:
                res[idx] = min_heap[0][0]

        return res