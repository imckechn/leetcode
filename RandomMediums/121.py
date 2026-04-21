class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        left = 0
        right = 0

        while right < len(prices)-1:
            right += 1

            if prices[right] >= prices[left]:
                total = max(total, prices[right] - prices[left])
            else:
                left = right

        return total
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))