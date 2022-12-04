# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def measure(root):
            if not root:
                return 0
            len_l = measure(root.left)
            len_r = measure(root.right)
            res[0] = max( len_l+len_r, res[0])
            return 1 + max(len_l, len_r)

        res = [0]  # list is mutable (pass by reference)
        measure(root)
        return res[0]