# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = [] # val, node
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        head = ListNode(0)
        curr = head
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        return head.next