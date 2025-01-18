from typing import List


class Solution:
    def isValidMutation(geneA, geneB):
        count = 0
        for i in range(8): #Since genes are 8 chars long
            if geneA[i] != geneB[i]:
                count += 1

        if count > 1:
            return False
        return True

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        
        currentBest = len(bank) + 1
        for i in range(len(bank)):
            if Solution.isValidMutation(startGene, bank[i]):
                bankCopy = bank.copy()
                newStart = bankCopy.pop(i)
                ans = Solution.minMutation(self, newStart, endGene, bankCopy)

                if ans < currentBest and ans != -1:
                    currentBest = ans

        if currentBest == len(bank) + 1:
            return -1
        return currentBest + 1


print(Solution.minMutation(None, "AACCGGTT", "AACCGGTA", ["AACCGGTA"])) #1
print(Solution.minMutation(None, "AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])) #2
print(Solution.minMutation(None, "AACCGGTT", "AACCGGTA", [])) #-1
