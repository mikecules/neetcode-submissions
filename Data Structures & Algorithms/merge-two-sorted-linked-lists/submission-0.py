# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1

        head = None
        current = None
        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val < current2.val and not head:
                head = current1
                current = head
                current1 = current1.next
                continue
            elif not head:
                head = current2
                current = head
                current2 = current2.next
                continue

            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next

            current = current.next

        while current1:
            current.next = current1
            current1 = current1.next
            current = current.next

        while current2:
            current.next = current2
            current2 = current2.next
            current = current.next

        current.next = None

        return head
