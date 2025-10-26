class SmallestInfiniteSet:
    def __init__(self):
        self.added = set()
        self.current = 1

    def popSmallest(self) -> int:
        if len(self.added) > 0 and min(self.added) < self.current:
            toBeDeleted = self.added.remove(min(self.added))
            
        else:
            toBeDeleted = self.current
            self.current += 1

        return toBeDeleted

    def addBack(self, num: int) -> None:
        if num not in self.added and num < self.current:
            self.added.add(num)


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

smol.addBack(1)
smol.addBack(2)
smol.addBack(3)
smol.addBack(4)
smol.addBack(5)
smol.addBack(6)
smol.addBack(7)


# set is [3,4,5.....]
# added is 1
# remove smallest

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)