# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric_tree(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return symmetric_tree(left.left, right.right) and \
                   symmetric_tree(left.right, right.left)
        if root:
            return symmetric_tree(root.left, root.right)
        else:
            return True
