from cmath import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.findGoodNodes(root, -inf)


    def findGoodNodes(self, root, largest):
        if not root:
            return 0

        if root.val >= largest:
            return 1 + self.findGoodNodes(root.left, max(largest, root.val)) + self.findGoodNodes(root.right, max(largest, root.val))
        else:
            return self.findGoodNodes(root.left, max(largest, root.val)) + self.findGoodNodes(root.right, max(largest, root.val))