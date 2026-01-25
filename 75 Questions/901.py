class StockSpanner:
    def __init__(self):
        self.monoStack = []
        
    def next(self, price: int) -> int:
        count = 1
        while len(self.monoStack) > 0 and self.monoStack[-1][0] <= price:
            oldPrice, oldCount = self.monoStack.pop()
            count += oldCount

        self.monoStack.append([price, count])
        return count