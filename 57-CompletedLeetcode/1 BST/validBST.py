class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def check(self, root, min, max):
        if root == None: 
            return True
        
        if max != None and root.val >= max:
            return False
        
        if min != None and root.val <= min:
            return False
        
        a = Solution.check(self, root.left, min, root.val) #left
        b = Solution.check(self, root.right, root.val, max) #right
        
        if not a or not b:
            return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        
        a = Solution.check(self, root.left, None, root.val) #left
        b = Solution.check(self, root.right, root.val, None) #right

        if not a or not b:
            return False
        return True
    

nodea = TreeNode(3)

nodeb = TreeNode(0)
nodea = TreeNode(2, None, nodea)
nodeb = TreeNode(1, nodeb, nodea)

# node = TreeNode(4)
# nodea = TreeNode(6)
# node = TreeNode(5, node, nodea)
node = TreeNode(3, nodeb)




print(Solution.isValidBST(None, node))