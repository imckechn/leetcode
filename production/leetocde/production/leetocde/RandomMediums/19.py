# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return head.next

        lead = head
        chaser = head

        counter = 0
        while lead.next:
            lead = lead.next
            if counter >= n:
                chaser = chaser.next
            counter += 1


        if counter < n:
            head = head.next
            return head
        
        elif counter == n:
            chaser = head

        if chaser.next != None:
            chaser.next = chaser.next.next
        else:
            chaser = None

        return head
    
sol = Solution()

a = ListNode(2)
b = ListNode(1, a)
c = ListNode(3, b)
d = ListNode(4, c)
e = ListNode(5, d)
f = ListNode(6, e)

# sol.removeNthFromEnd(b, 2)
sol.removeNthFromEnd(b, 1)