# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        left = Solution.findLongestZigZag(root, 0, True)
        right = Solution.findLongestZigZag(root, 0, False)
        return max(left, right) - 1
    
    def findLongestZigZag(root, longest, leftNext):
        if root == None:
            return 0
        
        currentLength = longest + 1
        leftLength = 0
        rightLength = 0

        if root.left != None:
            if leftNext:
                leftLength += Solution.findLongestZigZag(root.left, currentLength, not leftNext)
            else:
                leftLength += Solution.findLongestZigZag(root.left, 0, not leftNext)

        if root.right != None:
            if leftNext:
                rightLength += Solution.findLongestZigZag(root.right, 0, not leftNext)
            else:
                rightLength += Solution.findLongestZigZag(root.right, currentLength, not leftNext)

        return max(currentLength, max(leftLength, rightLength))

a = TreeNode(0)
sol = Solution()
sol.longestZigZag(a)