#Need to initialize a list of what's been deleted
#Create a list of what's been added, which has had to have been deleted

class SmallestInfiniteSet:
    def __init__(self):
        self.deleted = []
        self.added = []
        self.current = 1

    def addToDeleted(self, num):
        for i in range(len(self.deleted)):
            if self.deleted[i] > num:
                self.deleted.insert(i, num)
                return
        
        self.deleted.append(num)

    def popSmallest(self) -> int:
        if len(self.added) > 0 and self.added[0] < self.current:
            toBeDeleted = self.added.pop(0)
            
        else:
            toBeDeleted = self.current
            self.current += 1

        self.addToDeleted(toBeDeleted)
        return toBeDeleted

    def addBack(self, num: int) -> None:
        if num in self.deleted:
            self.deleted.remove(num)
            self.added.append(num)


smol = SmallestInfiniteSet()
smol.addBack(0)

smol.popSmallest()
smol.popSmallest()
smol.popSmallest()
smol.popSmallest()
smol.popSmallest()

smol.addBack(0)
smol.addBack(0)
smol.addBack(1)
smol.addBack(2)
smol.addBack(10)

smol.popSmallest()
smol.popSmallest()


# set is [3,4,5.....]
# added is 1
# remove smallest

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)