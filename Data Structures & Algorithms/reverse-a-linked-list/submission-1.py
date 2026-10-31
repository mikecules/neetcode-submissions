# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return head

    stack = []
    current = head

    while current:
      stack.append(current)
      current = current.next

    head.next = None
    head = stack.pop()
    current = head

    while current:
      if len(stack) == 0:
        return head

      current.next = stack.pop()
      current = current.next

    return head
