# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.smallest = None

    def goodNodes(self, root: TreeNode) -> int:
        return Solution.findGoodNodes(self, root, float(inf))
    

    def findGoodNodes(self, root, smallest)