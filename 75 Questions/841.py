from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        toVist = {}
        visited = {}

        for roomNumber, room in enumerate(rooms):
            toVist[roomNumber] = room

        self.visitRoom(0, visited, toVist)

        if len(visited.keys()) != len(toVist.keys()):
            return False
        return True
    
    def visitRoom(self, roomNumber, visited, toVisit):
        if roomNumber in visited:
            return

        visited[roomNumber] = toVisit[roomNumber]
        
        for num in visited[roomNumber]:
            self.visitRoom(num, visited, toVisit)