class Solution:
    def candy(ratings):
        n = len(ratings)
        candies = [1] * n 

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
    
        
    
    
# print(Solution.candy([1,0,2])) #5
# print(Solution.candy([1,2,2])) #4
# print(Solution.candy([1,3,2,2,1])) #7
print(Solution.candy([29,51,87,87,72,12])) #12
 