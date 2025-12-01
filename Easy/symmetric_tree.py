"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        values = [root.val]
        queue = deque([root])
        while queue:
            if values != list(reversed(values)):
                return False 
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                if node.left:
                    values.append(node.left.val)
                else:
                    values.append(None)

                if node.right:
                    values.append(node.right.val)
                else:
                    values.append(None)

        return True


# This has time and space complexity O(n), where n is the number of nodes in the tree