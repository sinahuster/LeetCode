"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Constraints:
The number of nodes in the tree is in the range [1, 2 * 10^4].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        total = 0
        if low <= root.val and root.val <= high:
            total = root.val

        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)

        total += right + left

        return total
    
# This has time and space complexity O(n), where n is the number of roots in the tree