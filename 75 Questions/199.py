# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.numbers = []
        self.dfs(root, 1)
        return self.numbers
    
    def dfs(self, root, height):
        if not root:
            return
        
        if height > len(self.numbers):
            self.numbers.append(root.val)

        self.dfs(root.right, height+1)
        self.dfs(root.left, height+1)

