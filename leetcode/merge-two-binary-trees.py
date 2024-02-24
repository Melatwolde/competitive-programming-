# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:    
            newTree = TreeNode(root1.val + root2.val)
            newTree.left = self.mergeTrees(root1.left, root2.left)
            newTree.right = self.mergeTrees(root1.right, root2.right)
            return newTree
        else:
            return root1 or root2