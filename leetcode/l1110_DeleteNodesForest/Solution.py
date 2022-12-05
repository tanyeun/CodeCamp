from typing import Optional
from typing import List
from datastructure.my_tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def del_nodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        def delete(node, out):
            if not node:
                return None
            if node.val in to_delete:
                out += [delete(node.left, out)]
                out += [delete(node.right, out)]
                return None
            else:
                node.left = delete(node.left, out)
                node.right = delete(node.right, out)
                return node
        res += [delete(root, res)]
        return [i for i in res if i]
