"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where 
v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Constraints:
The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_min, curr_max):
            if not node:
                return curr_max - curr_min

            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            return max(dfs(node.left, curr_min, curr_max), dfs(node.right, curr_min, curr_max))

        return dfs(root, root.val, root.val)
        

# This has time and space complexity O(n) where n is the number of nodes the tree has 