from typing import List


class Solution:
    def updatePerms(elem, perms):
        for i in range(len(perms)):
            perms[i].insert(0, elem)

        return perms

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        found = []

        if len(nums) == 1:
            return nums

        base = nums[0]
        for i in range(len(nums)):
            elem = nums[0]

            perms = Solution.permuteUnique(self, nums[1:])

            #Add elem to perms
            perms = Solution.updatePerms(elem, perms)

            found += perms

            base = perms[0]
            base[0], base[1] = base[1], base[0]


        return found

print(Solution.permuteUnique(None, [1,1,2]))