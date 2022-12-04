# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        def getHeight(root):
            if root is None:
                return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))

        if self.isBalanced(root.left) and self.isBalanced(root.right) and \
                abs(getHeight(root.left) - getHeight(root.right)) <= 1:
            return True
        else:
            return False