# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum_ = 0
        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                self.sum_ +=node.val
            if node.val > low:
                helper(node.left)
            if node.val < high:
                helper(node.right)
        helper(root)
        return self.sum_