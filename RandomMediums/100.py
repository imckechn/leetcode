from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        elif p.val != q.val:
            return False
    
        return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)