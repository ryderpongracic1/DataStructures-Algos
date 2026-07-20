# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(node1, node2):
            head = ListNode(0)
            curr = head
            while node1 and node2:
                if node1.val < node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next
            if node1:
                curr.next = node1
            elif node2:
                curr.next = node2
            return head.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = None if i + 1 >= len(lists) else lists[i + 1]
                merged.append(mergeTwoLists(node1, node2))
            lists = merged

        return lists[0]