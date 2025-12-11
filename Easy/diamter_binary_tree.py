"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        height(root)

        return self.diameter
    
# This has time and space complexity of O(n), where n is the number of nodes in the tree