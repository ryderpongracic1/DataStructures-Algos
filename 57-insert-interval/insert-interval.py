class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i in range(len(intervals)):
            # curr starts after target completely finishes
            # target belongs here
            if intervals[i][0] > newInterval[1]:
                merged.append(newInterval)
                return merged + intervals[i:]

            # curr completely finishes before target starts
            # curr belongs here
            elif intervals[i][1] < newInterval[0]:
                merged.append(intervals[i])

            # curr starts before target finishes
            # or target starts before curr ends
            # = overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        merged.append(newInterval)
        return merged