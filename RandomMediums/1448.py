# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return int(Solution.findGoodNodes(self, root, float(-inf)))
    

    def findGoodNodes(self, root, largest):
        goodNodes = 0
        if root.val >= largest:
            goodNodes += 1

        if root.right != None:
            goodNodes += Solution.findGoodNodes(self, root.right, max(largest, root.val))

        if root.left != None:
            goodNodes += Solution.findGoodNodes(self, root.left, max(largest, root.val))

        return goodNodes