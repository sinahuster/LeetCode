"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        total = 0

        while queue:
            length = len(queue)
            deepest = True
            for _ in range(length):
                node = queue.popleft()

                if not node.left and not node.right:
                    total += node.val
                    
                if node.left:
                    queue.append(node.left)
                    deepest = False
                if node.right:
                    queue.append(node.right)
                    deepest = False

            if not deepest:
                total = 0

        return total


# This has time and space complexity O(n), where n is the number of nodes in the tree.