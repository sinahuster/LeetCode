"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high):
            if not root:
                return True
            
            if not (low < root.val < high):
                return False
            
            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
        

# This has time and space complexity O(n), where n is the number of nodes in the tree. 