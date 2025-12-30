"""
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

Constraints:
The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return 
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0

        while queue and distance < k:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for neighbour in [node.left, node.right, node.parent]:
                    if neighbour and neighbour not in seen:
                        seen.add(neighbour)
                        queue.append(neighbour)
                
            distance += 1

        return [node.val for node in queue]

# This has time and space complexity O(n)
