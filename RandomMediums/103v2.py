from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [[[root, 0]]]
        ans = []

        while True:
            node = level = None
            for i in range(len(queue)):
                if len(queue[i]) != 0:
                    node, level = queue[i].pop()
                    break
            
            if not node:
                break

            if level%2 == 0:
                if node.left:
                    if len(queue) > level+1:
                        queue[level+1].append([node.left, level+1])
                    else:
                        queue.append([[node.left, level+1]])
                if node.right:
                    if len(queue) > level+1:
                        queue[level+1].append([node.right, level+1])
                    else:
                        queue.append([[node.right, level+1]])

                if len(ans) > level:
                    ans[level].insert(0,node.val)
                else:
                    ans.append([node.val])
                
            else:
                
                if node.left:
                    if len(queue) > level+1:
                        queue[level+1].append([node.left, level+1])
                    else:
                        queue.append([[node.left, level+1]])
                if node.right:
                    if len(queue) > level+1:
                        queue[level+1].append([node.right, level+1])
                    else:
                        queue.append([[node.right, level+1]])

                if len(ans) > level:
                    ans[level].append(node.val)
                else:
                    ans.append([node.val])
        return ans
    


sol = Solution()

node = TreeNode(5)
node = TreeNode(2, node, None)
node2 = TreeNode(4)
node2 = TreeNode(3, None, node2)
node = TreeNode(1, node, node2)

print(sol.zigzagLevelOrder(node))