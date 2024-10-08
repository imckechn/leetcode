class Solution:
    def spiralOrder(matrix):
        output = []
        direction = 'Right'
        x = 0
        y = 0

        while True:
            if direction == 'Right':
                if matrix[y][x+1] and matrix[y][x+1] != -1:
                    output.append(matrix[y][x+1])
                    matrix[y][x+1] = -1
                    x += 1
                else:
                    direction = "Down"

            elif direction == "Down":
                if matrix[y+1][x] and matrix[y+1][x] != -1:
                    output.append(matrix[y+1][x])
                    matrix[y+1][x] = -1
                else:
                    direction = "left"
                
                y += 1

            elif direction == "left":
                if matrix[y][x-1] and matrix[y][x-1] != -1:
                    output.append(matrix[y][x-1])
                    matrix[y][x-1] = -1
                else:
                    direction = "up"

                x -= 1

            elif direction == "up":
                if matrix[y-1][x] and matrix[y-1][x] != -1:
                    output.append(matrix[y-1][x])
                    matrix[y-1][x] = -1
                else:
                    direction = "right"

                y -= 1

        




Solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

# [[1,2,3]
#  [4,5,6]
#  [7,8,9]
# ]