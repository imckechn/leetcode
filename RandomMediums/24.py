# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swap(a, b):
        if b == None:
            return a

        a.next = b.next
        b.next = a
        return b

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        swapNextTurn = True

        head = Solution.swap(head, head.next)
        pointer = head.next

        while pointer != None and pointer.next:
            if swapNextTurn:
                if pointer.next:
                    pointer.next = Solution.swap(pointer.next, pointer.next.next)
                else:
                    break
            
            swapNextTurn = not swapNextTurn
            pointer = pointer.next

        return head
    
a = ListNode(4)
b = ListNode(3, a)
c = ListNode(2, b)
d = ListNode(1, c)

sol = Solution()

sol.swapPairs(a)