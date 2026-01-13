from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0

        for elevation in gain:
            current += elevation
            highest = max(highest, current)

        return highest