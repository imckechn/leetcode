from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keyQueue = rooms[0]
        roomsVisited = {0: True}

        while keyQueue != []:
            key = keyQueue.pop(0)

            if key not in roomsVisited:
                roomsVisited[key] = True
                keyQueue += rooms[key]

        if len(roomsVisited.keys()) == len(rooms):
            return True
        return False



    
sol = Solution()

#Test 1
input = [[1],[2],[3],[]]
expected = True
ans = sol.canVisitAllRooms(input)
if ans == expected:
    print("Test 1: Passed")
else:
    print("Test 1: Failed, expected " + str(expected) + " but got " + str(ans))


#Test 2
input = [[1,3],[3,0,1],[2],[0]]
expected = False
ans = sol.canVisitAllRooms(input)
if ans == expected:
    print("Test 2: Passed")
else:
    print("Test 2: Failed, expected " + str(expected) + " but got " + str(ans))