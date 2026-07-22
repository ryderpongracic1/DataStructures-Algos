class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_mins(time):
            hour, minute = time.split(':')
            return (int(hour) * 60) + int(minute)

        
        for i, time in enumerate(timePoints):
            timePoints[i] = time_to_mins(time)

        timePoints.sort()
        res = (24 * 60) + 1
        prev = timePoints[0]

        for minutes in timePoints[1:]:
            res = min(res, minutes - prev)
            prev = minutes
        
        # rollover: (24 * 60) minutes in a day - latest time + earliest time
        # 23:59 to 00:02 is 3 min diff: 1440 - 1439 + 2 = 3
        res = min(res, (24 * 60) - timePoints[-1] + timePoints[0])
        return res