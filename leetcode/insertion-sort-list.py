# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack = sorted(stack)
        dummy = ListNode(0)
        temp = dummy
        for i in stack:
            temp.next = ListNode(i)
            temp = temp.next
        return dummy.next
        