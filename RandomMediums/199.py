# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [
            [root, 0]
        ]
        deepestLayerObserved = -1
        found = []
        
        while queue != []:
            pair = queue.pop(0)

            if pair[1] > deepestLayerObserved:
                deepestLayerObserved += 1
                found.append(pair[0].val)

            if pair[0].right:
                queue.append([pair[0].right, pair[1] + 1])
            if pair[0].left:
                queue.append([pair[0].left, pair[1] + 1])

        return found


