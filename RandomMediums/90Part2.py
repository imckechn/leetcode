from typing import List
import copy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = nums.sort()

        sets = [[]]

        for num in nums:
            setsCopy = copy.deepcopy(sets)
            for subset in sets:
                subset.append(num)

                if subset not in setsCopy:
                    setsCopy.append(subset)

            sets = copy.deepcopy(setsCopy)

        return sets



nums = [1,2,2]
Solution.subsetsWithDup(None, nums)