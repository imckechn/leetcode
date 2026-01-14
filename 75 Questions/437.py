# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         return self.findPathSum(root, targetSum, [])
    
#     def findPathSum(self, root, target, currentSums):
#         if root == None:
#             return 0
        
#         currentSums = [x + root.val for x in currentSums]
#         currentSums.append(root.val)

#         return currentSums.count(target) + self.findPathSum(root.left, target, currentSums[:]) + self.findPathSum(root.right, target, currentSums[:])

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        self.prefix = collections.defaultdict(int)
        self.prefix[0] = 1
        return self.dfs(root,0)

    def dfs(self,node,curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            path_ending_here = self.prefix.get(curr_sum-self.targetSum,0)

            self.prefix[curr_sum] += 1

            left = self.dfs(node.left,curr_sum)
            right = self.dfs(node.right,curr_sum)

            self.prefix[curr_sum] -= 1

            return path_ending_here + left + right
        


alpha = TreeNode(6)
a = TreeNode(10)
b = TreeNode(0, a, alpha)
c = TreeNode(5, b)
d = TreeNode(5, c)

sol = Solution()
print(sol.pathSum(d, 10)) #3