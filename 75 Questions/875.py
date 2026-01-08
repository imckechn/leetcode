from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        low = 1
        high = piles[-1]
        mid = (high+low)//2

        hoursNeeded = self.eat(piles, mid)

        while hoursNeeded != h:
            if hoursNeeded < h:
                high = mid-1
            else:
                low = mid+1
            
            mid = (high+low)//2
            hoursNeeded = self.eat(piles, mid)
        
        return mid

    def eat(self, piles, quantity):
        count = 0
        index = -1
        left = 0
        pilesLength = len(piles)

        while True:
            if left <= 0:
                index += 1
                
                if index >= pilesLength:
                    break
                left = piles[index]
            else:
                count += 1
                left -= quantity
        return count
    

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            
            if total_hours <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

sol = Solution()
print(sol.minEatingSpeed([312884470], 312884469))
print(sol.minEatingSpeed([3,6,7,11], 8))