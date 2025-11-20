import random


class RandomizedSet:
    def __init__(self):
        self.elements = {}

    def insert(self, val: int) -> bool:
        try:
            if self.elements[val]:
                return False
        except:
            self.elements[val] = True
            return True

    def remove(self, val: int) -> bool:
        try:
            self.elements.pop(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        keys = list(self.elements.keys())
        index = random.randint(0, len(keys))
        return keys[index]
        


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