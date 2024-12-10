# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def visitNodes(root, queue, answers):
        level = root[1]
        node = root[0]
        if node == None: 
            if len(queue) == 0:
                return []
            else:
                return Solution.visitNodes(queue.pop(0), queue, answers)

        queue.append([node.left, level+1])
        queue.append([node.right, level+1])

        if root[1] >= len(answers):
            answers.append([])

        answers[root[1]].append(node.val)

        return Solution.visitNodes(queue.pop(0), queue, answers)



    def levelOrder(root):
        queue = []
        answers = []
        Solution.visitNodes([root, 0], queue, answers)
        return answers
        

nodea = TreeNode(9)
nodeb = TreeNode(15)
nodec = TreeNode(7)
noded = TreeNode(20, nodeb, nodec)
root = TreeNode(3, nodea, noded)

ans = Solution.levelOrder(root)

print(ans)