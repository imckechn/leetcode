class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def mustBeSmallerBST(self, root, min, max): # Left
        if root == None: 
            return True

        if root.left != None and (root.left.val >= root.val or root.left.val >= max):
            return False
        elif root.right != None and (root.right.val <= root.val or root.right.val >= max) :
            return False
        
        max = root.val
        
        a = Solution.mustBeLargerBST(self, root.left, min, max)
        b = Solution.mustBeSmallerBST(self, root.right, min, max)

        if not a or not b:
            return False
        return True
    
    def mustBeLargerBST(self, root, min, max): # Right
        if root == None: 
            return True

        if root.left != None and (root.left.val >= root.val or root.left.val <= min):
            return False
        elif root.right != None and (root.right.val <= root.val or root.right.val <= min):
            return False
        
        max = root.val
        
        a = Solution.mustBeLargerBST(self, root.left, min, max)
        b = Solution.mustBeSmallerBST(self, root.right, min, max)

        if not a or not b:
            return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True

        if root.left != None and root.left.val >= root.val:
            return False
        elif root.right != None and root.right.val <= root.val:
            return False
        
        a = Solution.mustBeSmallerBST(self, root.left, root.val, root.val)
        b = Solution.mustBeLargerBST(self, root.right, root.val, root.val)

        if not a or not b:
            return False
        return True
    

nodea = TreeNode(1)
nodeb = TreeNode(3)
nodec = TreeNode(6)
noded = TreeNode(4, nodeb, nodec)
root = TreeNode(5, nodea, noded)

nodea = TreeNode(0)
nodeb = TreeNode(2)
nodec = TreeNode(1, nodea, nodeb)

nodea = TreeNode(4)
nodeb = TreeNode(6)
noded = TreeNode(5, nodea, nodeb)
root = TreeNode(3, nodec, noded)



nodec = TreeNode(4)

nodea = TreeNode(3)
nodeb = TreeNode(7)
noded = TreeNode(6, nodea, nodeb)
root = TreeNode(5, nodec, noded)


node = TreeNode(27)
node = TreeNode(19, None, node)
node = TreeNode(26, node)
node2 = TreeNode(56)
node2 = TreeNode(47, None, node2)
node = TreeNode(32, node, node2)


node = TreeNode(27)
node = TreeNode(19, None, node)
node = TreeNode(26, node)
node = TreeNode(32, node)

print(Solution.isValidBST(None, node))