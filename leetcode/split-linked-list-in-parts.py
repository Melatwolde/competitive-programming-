# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        part = length // k
        rem = length % k

        curr = head
        res = []

        for i in range(k):
            part_head = curr
            part_len = part + 1 if i < rem else part
            for j in range(part_len - 1):
                if curr:
                    curr = curr.next
            if curr:
                nextnode = curr.next
                curr.next = None
                curr = nextnode
            res.append(part_head)

        return res