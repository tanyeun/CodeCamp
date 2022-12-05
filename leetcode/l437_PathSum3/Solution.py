# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def root_sum(node, target):
            if node is None:
                return 0
            count = 1 if node.val == target else 0
            count += root_sum(node.left, target - node.val)
            count += root_sum(node.right, target - node.val)
            return count

        output = 0
        if root:
            output = root_sum(root, targetSum) + self.pathSum(root.left, targetSum) + \
                     self.pathSum(root.right, targetSum)
        return output
