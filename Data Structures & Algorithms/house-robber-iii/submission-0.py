# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = 0
        def maxAmount(node):
            if not node:
                return [0,0]
            
            left = maxAmount(node.left)
            right = maxAmount(node.right)
            withroot = node.val + left[1] + right[1]
            withoutroot = max(left) + max(right)
            return [withroot,withoutroot]
        
        return max(maxAmount(root))