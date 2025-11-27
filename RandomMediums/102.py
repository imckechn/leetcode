from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[root, 0]]
        ans = []

        while queue != []:
            node, level = queue.pop()

            if node.right: queue.append([node.right, level+1])
            if node.left: queue.append([node.left, level+1])

            if len(ans) > level:
                ans[level].append(node.val)
            else:
                ans.append([node.val])
        return ans
    

sol = Solution()

node = TreeNode(5)
node = TreeNode(2, None, node)
node2 = TreeNode(4)
node2 = TreeNode(3, None, node2)
node = TreeNode(1, node, node2)

sol.levelOrder(node)