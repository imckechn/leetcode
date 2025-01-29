class Solution:
    def canCompleteCircuit(gas, cost):
        tank = 0
        indexBeingTested = 0
        currentIndex = 0
        currentLoop = True
        maxLen = len(gas)

        while(True):
            tank += gas[currentIndex]

            if tank - cost[currentIndex] < 0:
                if currentIndex < indexBeingTested or currentIndex + 1 > maxLen:
                    return -1

                indexBeingTested = currentIndex + 1
                tank = 0
                currentLoop = True

            else:
                tank -= cost[currentIndex]

            if indexBeingTested == currentIndex and currentLoop == False:
                return indexBeingTested

            currentIndex += 1
            
            if currentIndex == maxLen:
                currentLoop = False
                currentIndex = 0
            


print(Solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) #3
print(Solution.canCompleteCircuit([2,3,4], [3,4,3])) #3
