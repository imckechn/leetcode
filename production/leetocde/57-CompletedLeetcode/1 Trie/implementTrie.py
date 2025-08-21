# Approach was write, initial data storage was wrong, should have only used dictionary instead of a val as well. Would have been faster

class Trie:
    def __init__(self):
        self.val = ""
        self.children = {}

    def insert(self, word: str) -> None:
        if self.val == word:
            self.children[""] = Trie()
            return

        nextWord = self.val + list(word)[len(self.val)]

        if nextWord not in self.children.keys():
            self.children[nextWord] = Trie()
            self.children[nextWord].val = nextWord

        return Trie.insert(self.children[nextWord], word)

    def search(self, word: str) -> bool:
        if word == self.val and "" in self.children.keys():
            return True

        nextWord = ''.join(list(word)[:len(self.val)+1])

        if nextWord in self.children.keys():
            return Trie.search(self.children[nextWord], word)
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix == self.val:
            return True

        nextWord = ''.join(list(prefix)[:len(self.val)+1])

        if nextWord in self.children.keys():
            return Trie.startsWith(self.children[nextWord], prefix)
        else:
            return False

trie = Trie() #null
print("None")
print(trie.insert("apple")) #null
# print(trie.search("apple")) #true
# print(trie.search("app")) #false
print(trie.startsWith("app")) # true
print(trie.insert("app")) #null
print(trie.search("app")) #true

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)