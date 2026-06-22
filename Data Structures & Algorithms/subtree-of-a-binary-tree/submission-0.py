# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main root is empty, it can't contain any subRoot (since subRoot has at least 1 node per constraints)
        if not root:
            return False
        
        # If the current trees are identical, we found a match
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check the left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they are identical
        if not p and not q:
            return True
        # If only one node is null, or their values don't match, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check if both left and right children are also identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)