# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.recover(root, -inf, inf)
    
    def recover(self, root, min, max):
        if not root:
            return
        
        self.recoverTree(root.right, root.val, max)
        self.recoverTree(root.left, min, root.val)
        
        if root.left and (root.left.val > root.val or left.val):
            root.val, root.left.val = root.left.val, root.val
        elif root.right and root.right.val < root.val:
            root.val, root.right.val = root.right.val, root.val
        return

rightChild = TreeNode(3)
right = TreeNode(4, rightChild)
left = TreeNode(1)
head = TreeNode(2, left, right)
sol = Solution()

sol.recoverTree(head)
