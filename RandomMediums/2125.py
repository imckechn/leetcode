from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        row = 0
        ans = 0
        number = 1
        prev = 0

        sums = [row.count("1") for row in bank]
        sumsLen = len(sums)
        
        i = 0
        for i in range(sumsLen):
            if sums[i] != 0:
                number *= sums[i]
                prev = i
                break

        row = i+1
        while row < sumsLen:
            if sums[row] == 0:
                row += 1
                continue
            number *= sums[row]
            ans += number
            number /= sums[prev]
            prev = row
            row += 1

        return int(ans)
    

sol = Solution()

#Test 1
bank = ["011001","000000","010100","001000"]
expected = 8
ans = sol.numberOfBeams(bank)

if ans != expected:
    print("T1 failed")
else:
    print("T1 passed")

#Test 2
bank = ["000","111","000"]
expected = 0
ans = sol.numberOfBeams(bank)

if ans != expected:
    print("T2 failed")
else:
    print("T2 passed")