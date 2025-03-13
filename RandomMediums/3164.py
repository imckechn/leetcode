from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1.sort()
        nums2.sort()

        mem = {}

        pairs = 0

        for num in nums1:
            if num in mem.keys():
                pairs += mem[num]
                continue

            total = 0

            for second in nums2:
                if second == 0:
                    continue

                if num >= second*k:
                    if num % (second*k) == 0:
                        pairs += 1
                        total += 1
                else:
                    break

            mem[num] = total

        return pairs


print(Solution.numberOfPairs(None, [70,70], [6,10], 7))