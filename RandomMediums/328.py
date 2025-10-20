
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        oddPointer = head
        evenPointer = head.next

        nextPointerIsEven = False
        while evenPointer.next != None:
            if nextPointerIsEven:
                evenPointer = evenPointer.next
            
            else:
                nextOdd = evenPointer.next
                evenPointer.next = nextOdd.next
                nextOdd.next = oddPointer.next
                oddPointer.next = nextOdd
                oddPointer = oddPointer.next

            nextPointerIsEven = not nextPointerIsEven

        return head
