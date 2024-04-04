# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, 0, 0)]) 
        res = 0
        prevnum, prelevel = 0, 0
        
        while q:
            node, num, level = q.popleft()
            
            if level > prelevel:
                prelevel = level
                prevnum = num
            
            res = max(res, num - prevnum + 1)
            
            if node.left:
                q.append((node.left, num * 2, level + 1)) 
            if node.right:
                q.append((node.right, num * 2 + 1, level + 1)) 
        
        return res