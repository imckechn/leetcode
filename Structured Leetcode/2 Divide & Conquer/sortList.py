# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def getLastNode(head):
        if head.next == None:
            return head
        return Solution.getLastNode(head.next)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: #Need to run a quick sort algo on this
        last = Solution.getLastNode(head)

        if last == head:
            return

        pointerA = head
        pointerB = head

        while(pointerB != last):
            pointerB = pointerB.next

            if pointerB.val < last.val:
                
                pointerA = pointerA.next
                if pointerA.val > last.val:
                    pointerA.val, pointerB.val = pointerB.val, pointerA.val


        return       

nodea = ListNode(4)
nodeb = ListNode(2, nodea)
nodec = ListNode(3, nodeb)
noded = ListNode(1, nodec)

Solution.sortList(None, noded)