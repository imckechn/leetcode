class StockSpanner:
    def __init__(self):
        self.elems = []
        

    def next(self, price: int) -> int:
        count = 1

        while len(self.elems) != 0 and self.elems[-1][0] <= price:
            count += self.elems[-1][1]
            self.elems.pop()

        self.elems.append([price, count])
        return count


#Test
stockSpanner = StockSpanner()

ans = stockSpanner.next(100); # return 1
if ans != 1:
    print("Failed")
ans = stockSpanner.next(80); # return 1
if ans != 1:
    print("Failed")
ans = stockSpanner.next(60); # return 1
if ans != 1:
    print("Failed")
ans = stockSpanner.next(70); # return 1
if ans != 2:
    print("Failed")
ans = stockSpanner.next(60); # return 1
if ans != 1:
    print("Failed")
ans = stockSpanner.next(75); # return 1
if ans != 4:
    print("Failed")
ans = stockSpanner.next(85); # return 1
if ans != 6:
    print("Failed")

print("PASSED")