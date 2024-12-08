# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def rightSideView(root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        stack = [root.val]

        leftStack = Solution.rightSideView( root.left)
        rightStack = Solution.rightSideView(root.right)

        biggest = max(len(leftStack), len(rightStack))

        for i in range(biggest):
            try: 
                stack.append(rightStack[i])
            except:
                stack.append(leftStack[i])

        return stack
    

node = TreeNode(5)
node = TreeNode(2, None, node)
node2 = TreeNode(4)
node2 = TreeNode(3, None, node2)
node = TreeNode(1, node, node2)

print(Solution.rightSideView(node))