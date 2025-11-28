from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] or inorder == []:
            return None

        head = TreeNode(preorder[0])

        leftInorder = inorder[:inorder.index(preorder[0])]
        rightInorder = inorder[inorder.index(preorder[0])+1:]

        leftPreorder = []
        rightPreorder = []

        for num in preorder:
            if num in leftInorder:
                leftPreorder.append(num)
            elif num != head.val:
                rightPreorder.append(num)

        head.left = self.buildTree(leftPreorder, leftInorder)
        head.right = self.buildTree(rightPreorder, rightInorder)
        return head
    
sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = sol.buildTree(preorder, inorder)
print(ans)