from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counts = {}
        self.unqiues = []
        for num in nums:
            if num in self.counts:
                if self.counts[num] == 1:
                    self.unqiues.remove(num)
                    self.counts[num] += 1
            else:
                self.counts[num] = 1
                self.unqiues.append(num)

        self.unqiues.sort()

    def showFirstUnique(self) -> int:
        if len(self.unqiues) != 0:
            return self.unqiues[0]
        else:
            return -1
        

    def add(self, value: int) -> None:
        if value in self.counts:
            if self.counts[value] == 1:
                self.unqiues.remove(value)
                self.counts[value] += 1
        else:
            self.counts[value] = 1
            self.unqiues.append(value)
        

firstUnique = FirstUnique([809])
# FirstUnique firstUnique = new FirstUnique([809]);
print(firstUnique.showFirstUnique()) #// return 809
print(firstUnique.add(809))          #// the queue is now [809,809]
print(firstUnique.showFirstUnique()) #// return -1