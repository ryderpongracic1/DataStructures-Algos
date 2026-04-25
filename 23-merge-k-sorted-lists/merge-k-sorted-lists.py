# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        i = 0
        for LL in lists:
            if LL:
                minHeap.append((LL.val, i, LL))
                i += 1
        heapq.heapify(minHeap)

        dummy = ListNode()
        curr = dummy

        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            if node.next:
                i += 1
                heapq.heappush(minHeap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next

        return dummy.next