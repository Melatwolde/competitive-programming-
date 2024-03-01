# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.stack = 0
        def helper(root,min_, max_):
            
            if root is None:
                return

            self.stack = max(self.stack,abs(max_ - root.val), abs(min_ - root.val)) 
            min_  = min(min_,root.val)
            max_ = max(max_, root.val)
            
            
            helper(root.left, min_, max_)
            helper(root.right, min_, max_)
            # print(self.stack)
        helper(root,root.val,root.val)
        return self.stack
                # helper(root.left)
                # stack.append(root.val)
                # helper(root.right)
        # helper(root)
        