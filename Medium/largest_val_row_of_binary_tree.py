"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        largest = []

        while queue:
            length = len(queue)
            curr_max = float("-inf")

            for _ in range(length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            largest.append(curr_max)

        return largest
    
# This has time and space complexity O(n)
