from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    trees = []

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.trees = []
        numberSet = [i+1 for i in range(n)]
        tree = [0] * ((2**n)-1)
        for i in range(len(numberSet)):
            tree[0] = numberSet[i]
            self.backTrackTreeGen(tree, numberSet[:i] + numberSet[i+1:])

        return self.trees
    
    def backTrackTreeGen(self, tree, numberSet):
        length = len(numberSet)

        if length == 0:
            self.trees.append(tree.copy())
            return
        else:
            for i in range(len(tree)):
                if tree[i] == 0:
                    if i%2 == 0:
                        for j in range(length):
                            if tree[i//2-1] != 0 and tree[i//2-1] < numberSet[j]:
                                tree[i] = numberSet[j]
                                self.backTrackTreeGen(tree, numberSet[:j] + numberSet[j+1:])
                        tree[i] = 0

                    else:
                        for j in range(length):
                            if tree[(i-1)//2] != 0 and tree[(i-1)//2] > numberSet[j]:
                                tree[i] = numberSet[j]
                                self.backTrackTreeGen(tree, numberSet[:j] + numberSet[j+1:])
                        tree[i] = 0


sol = Solution()
# sol.generateTrees(1)
# sol.generateTrees(2)
print(sol.generateTrees(3))

            
