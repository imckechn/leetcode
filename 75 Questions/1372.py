# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.zigZag(root.left, False, 0), self.zigZag(root.right, True, 0))

    def zigZag(self, root, isRightNode, count):
        if not root:
            return count

        if isRightNode:
            largest = max(self.zigZag(root.left, False, count + 1), self.zigZag(root.right, True, 0))
        else:
             largest = max(self.zigZag(root.left, False, 0), self.zigZag(root.right, True, count + 1))
        return max(largest, count)