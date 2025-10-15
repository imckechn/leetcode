# Definition for a binary tree node.
from typing import List, Optional
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        numbers = []


        for i in range(1, n+1):
            numbers.append(i)

        variations = list(Solution.generateVariations(numbers))

        trees = set()

        for lst in variations:
            trees.add(Solution.createTree(lst))

        return trees

    def createTree(lst):
        root = TreeNode(lst[0])

        for elem in lst[1:]:
            Solution.appendToTree(root, elem)
        
        return root
    
    def appendToTree(root, elem):
        while True:
            if root.val < elem:
                if root.right == None:
                    root.right = TreeNode(elem)
                    break
                else:
                    root = root.right 
            else:
                if root.left == None:
                    root.left = TreeNode(elem)
                    break
                else:
                    root = root.left 


    def generateVariations(numbers):
        if len(numbers) <= 1:
            yield numbers
            return

        for num in Solution.generateVariations(numbers[1:]):
            for i in range(len(numbers)):
                yield num[:i] + numbers[0:1] + num[i:]


Solution.generateTrees(None, 3)