# Graph shortest path — BFS
# Start from '0000' and expand to ans
# Only queue safe combinations
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        deadends.add('0000')
        queue = collections.deque([('0000', 0)])

        while queue:
            lock, count = queue.popleft()
            if lock == target:
                return count

            for i in range(len(lock)):
                digit = str((int(lock[i]) + 1) % 10)
                newLock = lock[:i] + digit + lock[i + 1:]
                if newLock not in deadends:
                    queue.append((newLock, count + 1))
                    deadends.add(newLock)

                digit = str((int(lock[i]) - 1) % 10)
                newLock = lock[:i] + digit + lock[i + 1:]
                if newLock not in deadends:
                    queue.append((newLock, count + 1))
                    deadends.add(newLock)
        return -1