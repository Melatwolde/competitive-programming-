# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr= ListNode(0)  
        curr.next = head
        print(curr)
        l , r = curr , curr

        
        for _ in range(n):
            r = r.next

        while r.next is not None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return curr.next