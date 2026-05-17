import heapq
from collections import defaultdict, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int) # A-Z task -> frequency
        for t in tasks:
            counts[t] += 1
        
        # max heap of currently-available tasks by frequency
        # top is greedy choice
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # next_time_available, remaining_count

        while max_heap or queue:
            time += 1
            if queue and queue[0][0] <= time:
                _, cnt = queue.popleft()
                heapq.heappush(max_heap, cnt)
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt < 0:
                    queue.append((time + n + 1, cnt))
        return time