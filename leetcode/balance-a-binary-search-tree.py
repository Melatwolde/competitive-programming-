# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def helper(root):
            if not root:
                return 
            helper(root.left)
            ans.append(root.val)
            helper(root.right) 
            return ans

        helper(root)
           
        def back(left, right):
            if left > right:
                return

            mid =(left + right) // 2
            root = TreeNode(ans[mid])
            root.left = back(left , mid-1)
            root.right = back( mid + 1, right)

            return root
        return back( 0 , len(ans)-1)

        
        
        