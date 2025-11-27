# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    location = None
    changeMade = True

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        while self.changeMade:
            self.changeMade = False
            self.location = None
            self.recover(root, -inf, inf)
            
    def recover(self, root, min, max):
        if root.val > max:
            self.location = [root, max]
            return
        elif root.val < min:
            self.location = [root, min]
            return
        
        if root.left: self.recover(root.left, min, root.val)
        if root.right: self.recover(root.right, root.val, max)

        if self.location and self.location[1] == root.val:
            root.val, self.location[0].val = self.location[0].val, root.val
            self.changeMade = True


sol = Solution()

# rightChild = TreeNode(3)
# right = TreeNode(4, rightChild)
# left = TreeNode(1)
# head = TreeNode(2, left, right)

left = TreeNode(3)
right = TreeNode(2)
head = TreeNode(1, left, right)

sol.recoverTree(head)
