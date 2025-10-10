# Definition for a binary tree node.
from typing import List, Optional
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    #Generate every possible compination of n numbers
    # Generate trees for each combination in order of the values as they appear in the array

    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)

        variations = []
        for i in range(n):
            variations += Solution.generateVariations(numbers, 0)

    def generateVariations(numbers, depth):
        if depth == len(numbers)-1:
            return [copy.deepcopy(numbers)]

        numbers[depth], numbers[depth+1] = numbers[depth+1], numbers[depth]

        return Solution.generateVariations(numbers, depth + 1) + [copy.deepcopy(numbers)]
    

    # def buildTree(root, values):




Solution.generateTrees(None, 5)