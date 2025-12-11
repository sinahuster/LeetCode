"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        seen = []
        queue = deque([root])
        while queue:
            num = len(queue)
            seen.append(queue[-1].val)
            for _ in range(num):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return seen
    

# This has time and space complexity O(n), where n is the number of nodes