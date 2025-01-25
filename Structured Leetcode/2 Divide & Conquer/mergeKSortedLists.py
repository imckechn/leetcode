from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLowestValue(lists):
        lowest = lists[0].val

        for i in range(1, len(lists)):
            if lists[i].val < lowest:
                lowest = lists[i].val

        return lowest

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        currentLowest = Solution.getLowestValue(lists)
        nextLowest= 192839182918273

        answer = ListNode()
        current = answer
        
        while(len(lists) != 0):
            i = -1
            while (i != len(lists)):
                i += 1

                if i == len(lists):
                    break

                if lists[i].val == currentLowest:
                    copy = lists[i]
                    lists[i] = lists[i].next
                    current.next = copy
                    current = current.next

                    if lists[0] == None:
                        lists.pop(0)
                        i -= 1
                        continue

                
                if lists[i] != None and lists[i].val < nextLowest:
                    nextLowest = lists[i].val

            currentLowest = nextLowest
            nextLowest= 192839182918273

        return answer.next
    

nodeA = ListNode(3)
nodeb = ListNode(2, nodeA)
nodec = ListNode(1, nodeb)

nodex = ListNode(4)
nodey = ListNode(3, nodex)
nodez = ListNode(1, nodey)

nodee = ListNode(6)
nodef = ListNode(2, nodee)

Solution.mergeKLists(None, [nodec, nodez, nodef])