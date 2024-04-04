# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        point = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                point = slow
                break
        
        if not point:
            return None
        
        pt1 = head
        pt2 = point
        
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        
        return pt1