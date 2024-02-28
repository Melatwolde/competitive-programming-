# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev =  None
        curr = slow
        while curr:
            newnode = curr.next
            curr.next = prev
            prev = curr
            curr = newnode
        first = head
        sec = prev
        while sec:
            if first.val != sec.val:
                return False
            first = first.next
            sec = sec.next
        return True
        
            
