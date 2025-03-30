# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def fixTree(root, largest, smallest):
        if root == None:
            return False
        
        if root.left != None:
            if root.val < root.left.val or (smallest != None and root.left.val < smallest):
                root.val, root.left.val = root.left.val, root.val
                return True

        if root.right != None:
            if root.val > root.right.val or (largest != None and root.right.val > largest):
                root.val, root.right.val = root.right.val, root.val
                return True
        
        a = Solution.fixTree(root.left, root.val, smallest)
        b = Solution.fixTree(root.right, largest, root.val)
        
        return a or b

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans = Solution.fixTree(root, None, None)
        while ans:
            ans = Solution.fixTree(root, None, None)

        return


# a = TreeNode(2)
# b = TreeNode(3, None, a)
# c = TreeNode(1, b)

a = TreeNode(2)
b = TreeNode(4, a)
c = TreeNode(1)
d = TreeNode(3, c, b)



Solution.recoverTree(None, d)