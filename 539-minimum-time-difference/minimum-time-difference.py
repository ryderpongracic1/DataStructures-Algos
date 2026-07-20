class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # pigeon-hole
        if len(timePoints) > (24 * 60):
            return 0

        # buckets
        seen = [False] * (24 * 60)

        for t in timePoints:
            minutes = int(t[:2]) * 60 + int(t[3:])
            
            # already seen means diff is 0
            if seen[minutes]:
                return 0

            seen[minutes] = True

        res = float('inf')
        first = prev = -1 # track for 
        for minute, flag in enumerate(seen):
            # skip times we haven't seen
            if not flag:
                continue

            # only triggers once & saves first time seen
            if prev == -1:
                first = minute
            # bubbles min time
            else:
                res = min(res, minute - prev)

            # save prev as valid time
            prev = minute

        # check loop
        res = min(res, ((24 * 60) - prev) + first)

        return res