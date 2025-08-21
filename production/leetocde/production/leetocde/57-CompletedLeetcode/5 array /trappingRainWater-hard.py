class Solution:
    def trap(heights):
        if len(heights) < 3:
            return 0

        foundHeights = {} #key = found height, value = last index observed
        volumn = 0

        for i in range(len(heights)):
            elevation = heights[i]

            if i > 0 and heights[i-1] <= elevation:
                for j in reversed(sorted(foundHeights.keys())): #returns keys in highest to lowest
                    if j > elevation:
                        continue

                    if j == elevation:
                        volumn += elevation * (i - foundHeights[j] - 1)

                    if j < elevation:
                        if j < elevation:
                            volumn += j * (i - foundHeights[j] - 1)
                        else:
                            volumn += elevation * (i - foundHeights[j] - 1)

            if elevation != 0:
                foundHeights[elevation] = i


            # if i > 0 and height[i-1] <= elevation:
            #     for j in reversed(sorted(foundHeights.keys())):
            #         if j > elevation:
            #             continue
            #         else:
            #             if prev == -1:
            #                 prev = j
                        
            #             else:
            #                 if foundHeights[j] < foundHeights[prev]:
            #                     volumn += (prev - j) * (elevation -foundHeights[prev])
            #                     prev = j                        
            
            # if prev != -1:
            #     volumn += prev * (elevation - foundHeights[prev])

            # for i in range(elevation+1):  # Remove all heights smaller than 
            #     foundHeights.pop(i)

            

        return volumn

# print(Solution.trap([0,0,0,6,0,0])) #V1 Ans = 0
# print(Solution.trap([6,0,0,6])) #V2 ans = 12
# print(Solution.trap([1,0,6])) #V3 Ans = 1
print(Solution.trap([6,0,3,6])) #V4 Ans = 9
print(Solution.trap([6,0,3,0,6])) #V5 Ans = 15
print(Solution.trap([6,6,])) #V6 Ans = 0


  

print(Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
# print(Solution.trap([4,2,0,3,2,5]))