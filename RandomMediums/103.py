# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addChildrenToQueueEven(queue, node, level):
        if node.left != None:
            queue.append([node.left, level+1])

        if node.right != None:
            queue.append([node.right, level+1])

        return queue
    

    def addChildrenToQueueOdd(queue, node, level):
        if node.right != None:
            queue.append([node.right, level+1])

        if node.left != None:
            queue.append([node.left, level+1])

        return queue


    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == [] or root == None:
            return []

        values = [[root.val]]
        queue = Solution.addChildrenToQueueOdd([], root, 0)
        
        while len(queue) != 0:
            [node, level] = queue.pop(0)

            #record the node value
            if len(values) <= level:
                values.append([node.val])
            else:
                values[level].append(node.val)

            #append the children to the queue
            if level % 2 == 0:
                queue = Solution.addChildrenToQueueOdd(queue, node, level)
            else:
                queue = Solution.addChildrenToQueueEven(queue, node, level)

        return values



