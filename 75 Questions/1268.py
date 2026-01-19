from typing import List

class TreeNode:
    def __init__(self, val=""):
        self.val = val
        self.isEndNode = False
        self.children = []
        self.resetPointer()
        self.nextLetters = []

    def setEnd(self):
        self.isEndNode = True

    def getEnd(self):
        return self.isEndNode

    def resetPointer(self):
        self.pointer = 0

    def addChild(self, child):
        for i in range(len(self.nextLetters)):
            if child.val < self.nextLetters[i]:
                self.children.insert(i, child)
                self.nextLetters.insert(i, child.val)
                return

        self.children.append(child)
        self.nextLetters.append(child.val)

    def getNextChild(self):
        if len(self.children) > self.pointer:
            child = self.children[self.pointer]
            self.pointer += 1
            return child
        else:
            return None

class Solution:
    def addWordToTrie(self, head, word):
        current = head
        for letter in word:
            current.resetPointer()
            child = current.getNextChild()
            passed = False
            while child:
                if child.val == letter:
                    passed = True
                    break
                else:
                    child = current.getNextChild()

            if passed:
                current = child
            else:
                newLetter = TreeNode(letter)
                current.addChild(newLetter)
                current = newLetter

        current.setEnd()

    def dfs(self, node, wordSoFar):
        if node.getEnd():
            self.bigThree.append(wordSoFar+node.val)
            if len(self.bigThree) == 3:
                return -1
            
        node.resetPointer()
        child = node.getNextChild()
        while child:
            ans = self.dfs(child, wordSoFar + node.val)
            if ans == -1:
                return -1
            child = node.getNextChild()

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.bigThree = []
        head = TreeNode()
        
        for word in products:
            self.addWordToTrie(head, word)

        #Dfs words
        answer = []
        current = head
        wordSoFar = ""
        for letter in searchWord:
            current.resetPointer()
            child = current.getNextChild()
            passed = False
            while child:
                if child.val == letter:
                    passed = True
                    break
                else:
                    child = current.getNextChild()

            if passed:
                self.dfs(child, "")
                current = child
            answer.append([wordSoFar+x for x in self.bigThree])
            self.bigThree = []
            wordSoFar += letter

        return answer

sol = Solution()
print(sol.suggestedProducts(["mousepad", "mobile","mouse","moneypot","monitor"], "mouse"))