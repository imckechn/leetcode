#Need to initialize a list of what's been deleted
#Create a list of what's been added, which has had to have been deleted

class SmallestInfiniteSet:
    def __init__(self):
        self.deleted = []
        self.added = []
        self.current = 0

    def popSmallest(self) -> int:
        if self.deleted != []:
            self.deleted.append(self.current)
            self.current += 1
        
        else:
            self.deleted.append(self.current)
            self.current += 1

    def addBack(self, num: int) -> None:
        if num < self.current:
            if self.added == []:
                self.added.append(num)
            else:
                for i in range(len(self.added)):
                    if self.added[i] > num:
                        self.added.insert(i, num)
                        break


smol = SmallestInfiniteSet()

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