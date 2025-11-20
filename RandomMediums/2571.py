class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n = self.findClosest(n)

        return count
    
    def findClosest(self, n):
        largest = 0
        smallest = 0
        current = 1
        
        while True:
            if current >= n:
                largest = current
                break
            else:
                smallest = current
            current *= 2

        if n-smallest < largest-n:
            return n-smallest
        else:
            return largest-n
        

sol = Solution()
print(sol.minOperations(39))
print(sol.minOperations(54))

