from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        newHead = Node(head.val)
        
        oldCurrent = head
        newCurrent = newHead

        oldDict = {}
        newDict = {}

        counter = 0
        oldDict[oldCurrent] = counter
        newDict[counter] = newCurrent

        while oldCurrent.next != None:
            counter += 1

            oldCurrent = oldCurrent.next
            newCurrent.next = Node(oldCurrent.val)
            newCurrent = newCurrent.next

            oldDict[oldCurrent] = counter
            newDict[counter] = newCurrent

        oldCurrent = head
        newCurrent = newHead

        while oldCurrent != None:
            if oldCurrent.random != None:    
                index = oldDict[oldCurrent.random]
                newCurrent.random = newDict[index]

            oldCurrent = oldCurrent.next
            newCurrent = newCurrent.next

        return newHead