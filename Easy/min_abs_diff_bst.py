"""
Given the root of a Binary Search Tree (BST), 
return the minimum absolute difference between the values of any two different nodes in the tree.

Constraints:
The number of nodes in the tree is in the range [2, 10^4].
0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        nodes = []

        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        nodes.sort()

        ans = float("inf")
            
        for i in range(1, len(nodes)):
            ans = min(ans, nodes[i] - nodes[i - 1])
            
        return ans


# This has time and space complexity O(n) where n is the number of nodes in the tree