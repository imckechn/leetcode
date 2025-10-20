# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sequence = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        Solution.findLeafSequence(self, root1)
        leafSeq1 = self.sequence
        self.sequence = []

        Solution.findLeafSequence(self, root2)

        leafSeq2 = self.sequence
        return leafSeq1 == leafSeq2

    def findLeafSequence(self, root):
        if not root.right and not root.left:
            self.sequence.append(root.val)
            return
        
        else:
            if root.left != None:
                self.findLeafSequence(root.left)
            if root.right != None:
                self.findLeafSequence(root.right)

a = TreeNode(1)
b = TreeNode(1)


sol = Solution()
sol.leafSimilar( a, b)