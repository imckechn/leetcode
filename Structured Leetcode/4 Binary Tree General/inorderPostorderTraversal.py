# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Inorder
# Traverse Left
# Root
# Traverse Right

# PostOrder
# Traver Left
# Traverse Right
# Visit root
 
class Solution:
    def buildTree(inorder, postorder):
        if len(inorder) == 0: return None

        root = TreeNode(postorder[-1])

        splitIndex = inorder.index()
        inorder.remove(splitIndex)
        postorder.pop(-1)

        root.left = Solution.buildTree(inorder[:splitIndex], postorder[:splitIndex])
        root.right = Solution.buildTree(inorder[splitIndex:], postorder[splitIndex:])
        return root


inorderA = [9,3,15,20,7]
postOrderA = [9,15,7,20,3]

# inorderA = [1,2]
# postOrderA = [2,1]

# inorderA = [1,2,3]
# postOrderA = [3,2,1]

# inorderA = [2,3,1]
# postOrderA = [3,2,1]

# inorderA = [3,2,1]
# postOrderA = [3,2,1]

# inorderB = [-1]
# postOrderB = [-1]

Solution.buildTree(inorderA, postOrderA)
Solution.buildTree(inorderB, postOrderB)


