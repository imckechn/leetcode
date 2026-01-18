import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.currentPointer = 1
        self.addedBack = []
        

    def popSmallest(self) -> int:
        if len(self.addedBack) >= 1 and self.addedBack[0] < self.currentPointer:
            return heapq.heappop(self.addedBack)
        else:
            self.currentPointer += 1
            return self.currentPointer - 1
        

    def addBack(self, num: int) -> None:
        if num < self.currentPointer and num not in self.addBack:
            heapq.heappush(self.addedBack, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)