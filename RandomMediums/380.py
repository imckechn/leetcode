class RandomizedSet:

    def __init__(self):
        self.elements = set()

    def insert(self, val: int) -> bool:
       if self.elements.__contains__(val):
           return False
       else:
           self.elements.add(val)
           return True        

    def remove(self, val: int) -> bool:
        try:
            self.elements.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        elem =  self.elements.pop()
        self.elements.add(elem)
        return elem
        


# Your RandomizedSet object will be instantiated and called as such:
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print("Here")
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())