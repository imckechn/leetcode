# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = TreeNode(int(inf), root)
        parent = Solution.search(head, key)
        Solution.destory(parent, key)

        return head.left
    
    def destroy(parent, key):
        
    
    def search(head, key):
        if head.val < key:
           if head.left.val == key:
               return head
           
           else:
            return Solution.search(head.left, key) 

        else:
            if head.right.val == key:
                return head
            else:
                Solution.search(head.right, key)
    