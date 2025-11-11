# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = head
        follower = head

        if head.next == None:
            return None

        for i in range(n):
            leader = leader.next

        if not leader:
            return follower.next

        while leader.next != None:
            leader = leader.next
            follower = follower.next

        follower.next = follower.next.next
        return head
        


sol = Solution()

#Testing for the only node
ans = sol.removeNthFromEnd(ListNode(0), 1)
# Should be NONE

# #Testing last node if only one
a = ListNode(2)
b = ListNode(1, a)
ans = sol.removeNthFromEnd(b, 2)
# Should be 2

# remove the first node
a = ListNode(2)
b = ListNode(1, a)
ans = sol.removeNthFromEnd(b, 1)
# Should be 1

a = ListNode(5)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)
ans = sol.removeNthFromEnd(e, 2)
#Should be 1,2,3,5
