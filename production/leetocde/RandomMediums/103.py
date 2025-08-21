# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addChildrenRightSide(stack, node, level):
        if node.right != None:
            stack.insert(0, [node.right, level+1])

        if node.left != None:
            stack.insert(0, [node.left, level+1])

        return stack
    

    def addChildrenLeftSide(stack, node, level):
        if node.left != None:
            stack.insert(0, [node.left, level+1])

        if node.right != None:
            stack.insert(0, [node.right, level+1])

        return stack


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == [] or root == None:
            return []

        values = [[root.val]]
        queue = [Solution.addChildrenLeftSide([], root, 0)]
        
        rightToLeft = True
        while len(queue) != 0:
            stack = queue.pop(0)
            childStack = []

            while len(stack) > 0:
                [node, level] = stack.pop(0)

                if level < len(values):
                    values[level].append(node.val)
                else:
                    values.append([node.val])

                if rightToLeft:
                    childStack = Solution.addChildrenRightSide(childStack, node, level)
                else:
                    childStack = Solution.addChildrenLeftSide(childStack, node, level)

            rightToLeft = not rightToLeft

            if childStack != []:
                queue.append(childStack)
                    
        return values
    


a = TreeNode(15)
b = TreeNode(7)
c = TreeNode(20, a, b)
d = TreeNode(9)
e = TreeNode(3, d, c)

Solution.zigzagLevelOrder(None, e)