# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    # def checkBadValues(root):
    #     address = []
        
    #     if root == None or (root.left == None and root.right == None):
    #         return address

    #     #check no left
    #     if root.left == None:
    #         if root.val > root.right.val:
    #             address.append(root)
    #             return address + Solution.checkBadValues(root.right)

    #     #check no right
    #     if root.right == None:
    #         if root.val > root.left.val:
    #             address.append(root)
    #             return address + Solution.checkBadValues(root.left)

    #     #Need to check if it's a leaf node
    #     if root.val > root.left.val or root.val > root.right.val:
    #         address.append(root)

    #     return address + Solution.checkBadValues(root.left) + Solution.checkBadValues(root.right)

    #Need to run depth first search, then on your way back up, swap the values
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return
        
        Solution.recoverTree(None, root.left)
        Solution.recoverTree(None, root.right)

        if root.left != None and root.val > root.left.val:
            root.val, root.left.val = root.left.val, root.val

        if root.right != None and root.val > root.right.val:
            root.val, root.right.val = root.right.val, root.val

        return


a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3, a, b)

Solution.recoverTree(None, c)