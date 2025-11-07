from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        count = n * m
        prison = [["_" for y in range(n)] for x in range(m)]

        for wall in walls:
            prison[wall[0]][wall[1]] = "W"
            count -= 1

        for guard in guards:
            if prison[guard[0]][guard[1]] == "_":
                count -= 1

            prison[guard[0]][guard[1]] = "G"

            #Go left
            x = guard[1]-1
            y = guard[0]

            while x >= 0 and prison[y][x] != "W" and prison[y][x] != "G":
                if prison[y][x] != ".":
                    prison[y][x] = "."
                    count -= 1
                x -= 1

            #Go right
            x = guard[1]+1
            y = guard[0]

            while x < len(prison[0]) and prison[y][x] != "W" and prison[y][x] != "G":
                if prison[y][x] != ".":
                    prison[y][x] = "."
                    count -= 1
                x += 1

            #Go up
            x = guard[1]
            y = guard[0]-1

            while y >= 0 and prison[y][x] != "W" and prison[y][x] != "G":
                if prison[y][x] != ".":
                    prison[y][x] = "."
                    count -= 1

                y -= 1

            #Go down
            x = guard[1]
            y = guard[0]+1

            while y < len(prison) and prison[y][x] != "W" and prison[y][x] != "G":
                if prison[y][x] != ".":
                    prison[y][x] = "."
                    count -= 1
                y += 1

        return count
    

sol = Solution()

# #Test 1
# m = 4
# n = 6
# g = [[0,0],[1,1],[2,3]]
# w = [[0,1],[2,2],[1,4]]

# expected = 7
# ans = sol.countUnguarded(m, n, g, w)
# if ans == expected:
#     print("T1 passed")
# else:
#     print("T1 failed, got " + str(ans))

#Test 2
m = 2
n = 7
g = [[1,5],[1,1],[1,6],[0,2]]
w = [[0,6],[0,3],[0,5]]

expected = 1
ans = sol.countUnguarded(m, n, g, w)
if ans == expected:
    print("T2 passed")
else:
    print("T2 failed, got " + str(ans))