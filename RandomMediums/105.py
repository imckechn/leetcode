from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createTree(self, preorder, inorder, indexes, change):
        if preorder == [] or inorder == []:
            return None

        head = TreeNode(preorder[0])

        leftInorder = inorder[:change + indexes[preorder[0]]]
        rightInorder = inorder[change + indexes[preorder[0]]+1:]
        leftInorderHash = {}

        for left in leftInorder:
            leftInorderHash[left] = True

        leftPreorder = []
        rightPreorder = []

        for num in preorder:
            if num in leftInorderHash:
                leftPreorder.append(num)
            elif num != head.val:
                rightPreorder.append(num)

        head.left = self.createTree(leftPreorder, leftInorder, indexes, indexes[preorder[0]]+1)
        head.right = self.createTree(rightPreorder, rightInorder, indexes, indexes[preorder[0]])
        return head

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {}
        for i, num in enumerate(inorder):
            indexes[num] = i

        return self.createTree(preorder, inorder, indexes, 0)
    

class Solution:
    def buildTree(self, preorder, inorder):
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0

        def helper(start, end):
            if start > end:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            mid = idx_map[root_val]
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(inorder) - 1)

    
sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
ans = sol.buildTree(preorder, inorder)
print(ans)