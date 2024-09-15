class Solution:
    def trap(height):
        if len(height) < 3:
            return 0

        foundHeights = {} #key = found height, value = last index observed
        volumn = 0

        for i in range(len(height)):
            elevation = height[i]

            prev = -1
            j = -1
            if i > 0 and height[i-1] <= elevation:
                for j in reversed(sorted(foundHeights.keys())):
                    if j > elevation:
                        continue
                    else:
                        if prev == -1:
                            prev = j
                        
                        else:
                            if foundHeights[j] < foundHeights[prev]:
                                volumn += (prev - j) * (elevation -foundHeights[prev])
                                prev = j                        
            
            if prev != -1:
                volumn += prev * (elevation - foundHeights[prev])

            foundHeights[elevation] = i

        return volumn

                    

print(Solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution.trap([4,2,0,3,2,5]))