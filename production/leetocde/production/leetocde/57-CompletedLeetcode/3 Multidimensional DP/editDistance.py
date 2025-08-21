class Solution:
    def identifyIndexes(word1, word2):
        indexes = {}

        for i in range(len(word1)):
            if word1[i] in word2:
                if word1[i] in indexes.keys():
                    indexes[word1[i]].append(i)
                else:
                    indexes[word1[i]] = [i]

        return indexes
    

    def findOrder(indexes, word2):
        newIndexes = {}
        keys = list(indexes.keys())
        for i in range(1, len(keys)):
            if indexes[keys[i-1]] < indexes[keys[i]]:
                newIndexes[keys[i]] = [i]

        return newIndexes
    
    def doSwaps(indexes, word1, word2):
        wrd1 = list(word1)
        wrd2 = list(word2)
        keys = list(indexes.keys())
        
        changes, i, j, k = 0, 0, 0, 0
        while i != len(wrd1) and k != len(wrd2) and j != len(keys):
            if wrd1[i] != indexes[keys[j]]:
                if wrd2[k] != indexes[keys[j]]:
                    wrd1[i] = wrd2[k]
                    k += 1
                    changes += 1
            else:
                j += 1

            i += 1

        return wrd1, changes





    def minDistance(self, word1: str, word2: str) -> int:
        word1 = list(word1)
        indexes = Solution.identifyIndexes(word1, word2)

        indexes = Solution.findOrder(indexes, word2)

        wrd1, changes = Solution.doSwaps(indexes, word1, word2)


Solution.minDistance(None, "horse", "ros")
Solution.minDistance(None, "intention", "execution")