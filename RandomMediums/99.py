# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def checkBadValues(root):
        address = []
        
        if root == None or (root.left == None and root.right == None):
            return address

        #check no left
        if root.left == None:
            if root.val > root.right.val:
                address.append(root)
                return address + Solution.checkBadValues(root.right)

        #check no right
        if root.right == None:
            if root.val > root.left.val:
                address.append(root)
                return address + Solution.checkBadValues(root.left)

        #Need to check if it's a leaf node
        if root.val > root.left.val or root.val > root.right.val:
            address.append(root)

        return address + Solution.checkBadValues(root.left) + Solution.checkBadValues(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        values = Solution.checkBadValues(root)

        if len(values) > 2:
            print("Too many bad values")
            return
        else:
            values[0].val, values[1].val = values[1].val, values[0].val

a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(1, a, b)



print(Solution.recoverTree(None, c))