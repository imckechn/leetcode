from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newArr = []
        for num in nums:
            newArr.append(num*num)

        newArr.sort()
        return newArr