"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Constraints:
The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, level):
            if not node:
                return (-1, None)

            (left_depth, left) = dfs(node.left, level + 1)
            (right_depth, right) = dfs(node.right, level + 1)

            max_depth = 1 + max(right_depth, left_depth)

            if left_depth == right_depth:
                return (max_depth, node)
                
            elif left_depth > right_depth:
                return (max_depth, left)

            return (max_depth, right)

        max_level, connected = dfs(root, 0)

        return connected

# return the deepest level contained in the subtree and the node that is required to contain it

# This has time and space complexity O(n), where there are n nodes in the tree