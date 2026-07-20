class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert 'HH:MM' to minutes past 00:00
        for i in range(len(timePoints)):
            hour, minute = int(timePoints[i][:2]), int(timePoints[i][3:])
            timePoints[i] = (hour * 60) + minute

        timePoints.sort() # sort so the min diff is adjacent
        res = float('inf')

        # bubble min diff
        for i in range(1, len(timePoints)):
            diff = timePoints[i] - timePoints[i - 1]
            res = min(res, diff)

        # circular clock diff = (minutes in day - end time) + first time
        res = min(res, (24 * 60) - timePoints[-1] + timePoints[0])
        return res