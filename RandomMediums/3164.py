from typing import Counter, List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        freqs = Counter(num * k for num in nums2)
        counts = [0] * (max(nums1)+1)

        for num, count in freqs.items():
            for multiplier in range(num, len(counts), num):
                counts[multiplier] += count
        
        return sum(counts[num] for num in nums1)
    

print(Solution.numberOfPairs(None, [1,3,4], [1,3,4], 2))
print(Solution.numberOfPairs(None, [1,2,4,12], [2,4], 3))