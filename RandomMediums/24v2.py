# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        current = newHead

        while current.next != None and current.next.next != None:
            copy = current.next.next.next
            current.next.next.next = current.next
            current.next = current.next.next
            current.next.next.next = copy
            current = current.next.next

        return newHead.next



a = ListNode(3)
b = ListNode(2, a)
c = ListNode(1, b)

sol = Solution()
sol.swapPairs(c)