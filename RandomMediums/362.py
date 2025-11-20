class HitCounter:
    def __init__(self):
        self.counterStack = []
        self.currentTime = 0

    def hit(self, timestamp: int) -> None:
        self.counterStack.append(timestamp)
        self.getHits(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        self.currentTime = timestamp

        while len(self.counterStack) > 0 and self.currentTime - self.counterStack[0] >= 300:
            self.counterStack.pop(0)

        return len(self.counterStack)