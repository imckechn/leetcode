class Solution:
    def candy(ratings):
        totalCandies = 1
        currentCandyAmount = 2
        i = 1


        while(i < len(ratings)):
            if ratings[i-1] < ratings[i]:
                totalCandies += currentCandyAmount
                currentCandyAmount += 1
            elif ratings[i-1] >= ratings[i]:
                totalCandies += 1
                currentCandyAmount = 2
            
            i += 1

    
        return totalCandies
            

print(Solution.candy([1,0,2]))