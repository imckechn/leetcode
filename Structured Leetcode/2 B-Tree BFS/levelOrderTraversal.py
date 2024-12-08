# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def visitNodes(root, queue, answers, level):
        if root == None: answers

        queue.append(root.left)
        queue.append(root.right)

        if level > len(answers):
            answers.append([])

        answers[level].append(root.val)

        return Solution.visitNodes(queue.pop(0), queue, answers, )



    def levelOrder(root):
        queue = []
        answers = []
        queue, answers = Solution.visitNodes(root, queue, answers, 0)
        