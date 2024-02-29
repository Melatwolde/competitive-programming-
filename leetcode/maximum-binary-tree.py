# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left > right:
                return None
            
            new_ = max(nums[left:right+1])
            k = nums[left:right+1].index(new_) + left
            node = TreeNode(new_)
            node.left = helper(left, k-1)
            node.right = helper(k+1, right)

            return node

        return helper(0, len(nums) - 1)