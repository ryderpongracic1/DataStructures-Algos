# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
- Look at 2 lists at a time - merge them like mergeTwoLinkedLists
- Repeat until only 1 list remains
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []

            # look at 2 lists at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 >= len(lists):
                    l2 = None
                else:
                    l2 = lists[i + 1]
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        curr = head
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return head.next