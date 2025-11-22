# Definition for a binary tree node.
from typing import Optional

#Question was not clear, implied the numbers couldn't increase or decrease in a single span, learned from a test case you could.
# SUUPER ANNOYING

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    longest = 1

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root)
        return max(ans[1], self.longest)

    def dfs(self, root):
        if root.left == None and root.right == None:
            #root val, decreasing count, increasing count
            return [root.val, 1]
    
        rightChangeCount = 1
        leftChangeCount = 1

        r, l = None, None
        if root.right != None:
            r = self.dfs(root.right)
            if r[0]-1 == root.val or r[0]+1 == root.val:
                rightChangeCount += r[1]
        
        if root.left != None:
            l = self.dfs(root.left)
            if l[0]-1 == root.val or l[0]+1 == root.val:
                leftChangeCount += l[1]

        #Check if this isn't a parent node
        if r != None and l != None:
            if l[0]+1 == root.val and root.val == r[0]-1:
                self.longest = max(self.longest, (l[1] + r[1] + 1))
            elif l[0]-1 == root.val and root.val == r[0]+1:
                self.longest = max(self.longest, (l[1] + r[1] + 1))
        elif l != None:
            self.longest = max(self.longest, l[1])
        elif r != None:
            self.longest = max(self.longest, r[1])
        return [root.val, max(rightChangeCount, leftChangeCount)]