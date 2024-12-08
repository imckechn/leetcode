# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Inorder
# Traverse Left
# Root
# Traverse Right

# PostOrder
# Traver Left
# Traverse Right
# Visit root
 
class Solution:
    def buildTriple(inorder, postorder):
        if len(inorder) == 0:
            return None

        elif len(inorder) == 1:
            return TreeNode(inorder[0])

        elif len(inorder) == 2:
            if inorder[0] == postorder[0]:
                leaf = TreeNode(postorder[1])
                return TreeNode(postorder[0], leaf)
            
            else:
                leaf = TreeNode(postorder[1])
                return TreeNode(postorder[0], None, leaf)
            
        elif len(inorder) == 3:
            if inorder == postorder:
                leaf = TreeNode(inorder[0])
                leaf = TreeNode(inorder[1], leaf)
                return TreeNode(inorder[2], leaf)
            
            elif inorder[0] != postorder[0] and inorder[-1] == postorder[-1]:
                rightLeaf = TreeNode(postorder[0])
                leftLeaf = TreeNode(postorder[1], None, rightLeaf)
                return TreeNode(postorder[2], leftLeaf)

            else:
                leafA = TreeNode(postorder[0])
                leafB = TreeNode(postorder[1])
                return TreeNode(postorder[2], leafA, leafB)

    def buildLeft(inorder, postorder, leftNode):
        if len(inorder) < 4:
            return Solution.buildTriple(inorder, postorder)
        
        if len(inorder) == 4:
            leafA = TreeNode(postorder[0])
            leafB = TreeNode(postorder[1])
            rightLeaf = TreeNode(postorder[2], leafA, leafB)
            return TreeNode(postorder[3], leftNode, rightLeaf)

        return TreeNode(-1)
    

    def buildRight(inorder, postorder, rightNode):
        if len(inorder) < 4:
            return Solution.buildTriple(inorder, postorder)
        
        if len(inorder) == 4:
            leafA = TreeNode(postorder[0])
            leafB = TreeNode(postorder[1])
            leftLeaf = TreeNode(postorder[2], leafA, leafB)
            return TreeNode(postorder[3], leftLeaf, rightNode)

        return TreeNode(-1)



    def buildTree(inorder, postorder, ):
        root = None
        currentSpot = 0
        leftNode, rightNode = None, None
    
        while True:
            if inorder[currentSpot] == postorder[-1]:
                root = TreeNode(postorder[-1], leftNode)
                break

            elif inorder[currentSpot+1] == postorder[-1]:
                if currentSpot + 2 == len(postorder):
                    return Solution.buildLeft(inorder[currentSpot:currentSpot+2], postorder[currentSpot:currentSpot+2], leftNode)
                
                leftNode = TreeNode(inorder[currentSpot])
                root = TreeNode(postorder[-1], leftNode)
                currentSpot = currentSpot+1
                break

            elif inorder[currentSpot + 2] == postorder[-1]:
                if currentSpot + 3 == len(postorder):
                    return Solution.buildLeft(inorder[currentSpot:currentSpot+3], postorder[currentSpot:currentSpot+3], leftNode)

                lastSpot = len(postorder)-2
                leftNode = Solution.buildLeft(inorder[currentSpot:lastSpot+1], postorder[currentSpot:lastSpot+1], leftNode)
                root = TreeNode(postorder[-1], leftNode)
                currentSpot = currentSpot + 2
                break

            elif inorder[currentSpot] == postorder[currentSpot]:
                if inorder[currentSpot + 1] == postorder[-1]:
                    leftNode = TreeNode(inorder[currentSpot])
                    root = TreeNode(inorder[currentSpot+1], leftNode)
                    currentSpot = currentSpot+1
                    break

                else:
                    lastSpot = postorder.index(inorder[currentSpot+2])

            else:
                lastSpot =  postorder.index(inorder[currentSpot])

            leftNode = Solution.buildLeft(inorder[currentSpot:lastSpot+1], postorder[currentSpot:lastSpot+1], leftNode)
            currentSpot = lastSpot+1
        
        postorder.pop(-1)
        inorder.pop(currentSpot)
        
        while True:
            if currentSpot >= len(inorder):
                break
            
            elif currentSpot == len(inorder) -1:
                rightNode = TreeNode(inorder[currentSpot])
                break


            if inorder[currentSpot] == postorder[currentSpot]:
                lastSpot = postorder.index(inorder[currentSpot+1])

            else:
                lastSpot =  postorder.index(inorder[currentSpot])

            rightNode = Solution.buildRight(inorder[currentSpot:lastSpot+1], postorder[currentSpot:lastSpot+1], rightNode)
            currentSpot = lastSpot+1

        root.right = rightNode

        return root


# inorderA = [9,3,15,20,7]
# postOrderA = [9,15,7,20,3]

inorderA = [1,2]
postOrderA = [2,1]

# inorderA = [1,2,3]
# postOrderA = [3,2,1]

# inorderA = [2,3,1]
# postOrderA = [3,2,1]

# inorderA = [3,2,1]
# postOrderA = [3,2,1]

inorderB = [-1]
postOrderB = [-1]

Solution.buildTree(inorderA, postOrderA)
Solution.buildTree(inorderB, postOrderB)


