class Solution:
    def spiralOrder(matrix):
        output = [matrix[0][0]]
        matrix[0][0] = None
        direction = 'Right'
        y = 0
        x = 0
        maxY = len(matrix)
        maxX = len(matrix[0])
        

        while True:
            if len(output) == maxX * maxY:
                break

            if direction == "Right":
                if x + 1 != maxX and matrix[y][x+1] != None:
                    x += 1
                else:
                    direction = "Down"
                    continue
            
            elif direction == "Down":
                if y + 1 != maxY and matrix[y+1][x] != None:
                    y += 1
                else:
                    direction = "Left"
                    continue

            elif direction == "Left":
                if x - 1 != -1 and matrix[y][x-1] != None:
                    x -= 1
                else:
                    direction = "Up"
                    continue
                    
            else:
                if y - 1 != -1 and matrix[y-1][x] != None:
                    y -= 1
                else:
                    direction = "Right"
                    continue

            output.append(matrix[y][x])
            matrix[y][x] = None
        
        return output


print(Solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution.spiralOrder([[2,5],[8,4],[0,-1]]))

# [[1,2,3]
#  [4,5,6]
#  [7,8,9]
# ]