from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        


    def reverseLinkedList(head, end):
        first = head.next
        if first.next == None:
            first.next = head
            head.next = None

            return first
        
        second = first.next

        head.next, first.next = first.next, head
        head = first
        first = head.next

        while second != None or head.val == end:
            first.next = second.next
            second.next = head

            head = second
            second = first.next
            





a = ListNode(6)
b = ListNode(5, a)
c = ListNode(4, b)
d = ListNode(3, c)
f = ListNode(2, d)
g = ListNode(1, f)

Solution.reverseLinkedList(g)

Solution.reverseBetween(None, g, 2, 5)