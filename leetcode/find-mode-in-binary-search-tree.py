# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def helper(root):
            # if root == [0]:
            #     return  [0]

            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)

        freq = {}
        for val in res:
            freq[val] = freq.get(val, 0) + 1
        
        max_freq = max(freq.values()) if freq else 0
        modes = [val for val, freq in freq.items() if freq == max_freq]
        
        return modes