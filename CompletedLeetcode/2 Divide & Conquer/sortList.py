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
    
    def QS(head, last): #Need to perform same action, but when at the last node, see if you need to swap instead of automatically swapping
        if last == head or head == None or last == None:
            return

        newHead = ListNode(next=head)

        if last == head:
            return

        pointerA = newHead
        pointerB = newHead

        while(True):
            pointerB = pointerB.next

            if pointerB.val < last.val:
                pointerA = pointerA.next
                pointerA.val, pointerB.val = pointerB.val, pointerA.val

            elif pointerB.val == last.val:
                pivot = pointerA
                pointerA = pointerA.next

                if pointerA.val > pointerB.val:
                    pointerA.val, pointerB.val = pointerB.val, pointerA.val
                break

        Solution.QS(head, pivot)
        Solution.QS(pivot.next, last)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: #Need to run a quick sort algo on this
        newHead = ListNode(next=head)
        last = Solution.getLastNode(head)

        if last == head:
            return

        pointerA = newHead
        pointerB = newHead
        pivot = None

        while(True):
            pointerB = pointerB.next

            if pointerB.val < last.val:
                pointerA = pointerA.next
                pointerA.val, pointerB.val = pointerB.val, pointerA.val

            elif pointerB.val == last.val:
                pivot = pointerA
                pointerA = pointerA.next
                pointerA.val, pointerB.val = pointerB.val, pointerA.val
                break

        last, pointerA = pointerA, last

        Solution.QS(head, pivot)
        Solution.QS(pivot.next, Solution.getLastNode(head))

        return

nodea = ListNode(4)
nodeb = ListNode(2, nodea)
nodec = ListNode(1, nodeb)
noded = ListNode(3, nodec)

Solution.sortList(None, noded)