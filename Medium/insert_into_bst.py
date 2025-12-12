"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
You can return any of them.

Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-10^8 <= Node.val <= 10^8
All the values Node.val are unique.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root
        
        while True:
            if node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    break
            elif node.val < val:
                if node.right is not None:
                    node = node.right
                else:
                    break

        if node.val > val:
            node.left = TreeNode(val)
        if node.val < val:
            node.right = TreeNode(val)

        return root
    
# This has time complexity O(n), where n is the number of nodes in the tree, and space complexity O(1)
