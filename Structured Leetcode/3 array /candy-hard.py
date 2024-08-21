class Solution:

    def increasePreviousNumbers(candiesArr, ratings):
        for i in range(len(candiesArr) -1, -1, -1):
            candiesArr[i] = candiesArr[i] + 1
            if i != 0:
                if candiesArr[i-1] != candiesArr[i] or ratings[i] == ratings[i-1]:
                    break


    def candy(ratings):
        candiesArr = [1]

        for i in range (1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candiesArr.append(candiesArr[i-1] + 1)

            if ratings[i] == ratings[i-1]:
                candiesArr.append(1)

            if ratings[i] < ratings[i-1]:
                if candiesArr[i-1] == 1:
                    Solution.increasePreviousNumbers(candiesArr, ratings)
                    candiesArr.append(candiesArr[i-1] - 1)
                else:
                    candiesArr.append(1)

        total = 0
        for candy in candiesArr:
            total += candy

        return total
    
print(Solution.candy([1,0,2])) #5
print(Solution.candy([1,2,2])) #4
print(Solution.candy([1,3,2,2,1])) #7
print(Solution.candy([29,51,87,87,72,12])) #12
 