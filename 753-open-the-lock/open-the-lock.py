# BFS for shortest path
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        deadends.add('0000')

        queue = deque([('0000', 0)]) # lock, steps taken
        # Don't go back to start point

        while queue:
            lock, steps = queue.popleft()
            if lock == target:
                return steps
            for i in range(4):
                digit = (int(lock[i]) + 1) % 10
                new_lock = lock[:i] + str(digit) + lock[i + 1:]
                if new_lock not in deadends:
                    queue.append((new_lock, steps + 1))
                    deadends.add(new_lock) # Don't retrace steps

                digit = (int(lock[i]) - 1) % 10
                new_lock = lock[:i] + str(digit) + lock[i + 1:]
                if new_lock not in deadends:
                    queue.append((new_lock, steps + 1))
                    deadends.add(new_lock)
        return -1
