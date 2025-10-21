# Definition for a binary tree node.
from cmath import inf
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = TreeNode(float(inf), root)
        parent = Solution.search(head, key)

        if not parent:
            return head.left

        if parent.left and parent.left.val == key:
            parent.left = Solution.destroy(parent.left, key)
        else:
            parent.right = Solution.destroy(parent.right, key)  

        return head.left
    
    def destroy(toBeDeleted, key):
        #If it has no children
        if not toBeDeleted.left and not toBeDeleted.right:
            return None

        #If it only has one child
        if not toBeDeleted.left:
            return toBeDeleted.right

        if not toBeDeleted.right:
            return toBeDeleted.left

        #If it has both children
        current = toBeDeleted.left

        if not current.right:
            return current
        
        else:
            while current.right.right:
                current = current.right

            elem = current.right
            current.right = None
            elem.left = toBeDeleted.left
            elem.right = toBeDeleted.right
            return elem

    def search(head, key):
        if not head:
            return None
        
        if head.val > key:
           if head.left and head.left.val == key:
               return head
           else:
            return Solution.search(head.left, key) 

        else:
            if head.right and head.right.val == key:
                return head
            else:
                Solution.search(head.right, key)
    

root = TreeNode(1)
sol = Solution()
sol.deleteNode(root, 1)