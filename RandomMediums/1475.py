from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(0, len(prices)-1):
            j = i+1

            while j < len(prices):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
                else:
                    j += 1

        return prices