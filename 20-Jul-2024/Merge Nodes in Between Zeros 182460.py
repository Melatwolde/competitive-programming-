# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        sum = 0
        
        while head is not None:
            if head.val == 0:
                if sum > 0:
                    curr.next = ListNode(sum)
                    curr = curr.next
                    sum = 0
            else:
                sum += head.val
            head = head.next
            
        return dummy.next