from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        newHead = ListNode(0, head)
        current = newHead
        difference = right - left

        for i in range(left-1):
            current = current.next

        while difference != 0:
            self.sendRight(current, difference)
            difference -= 1

        return newHead.next
    
    def sendRight(self, node, steps):
        next = node.next

        for i in range(steps):
            if next.next == None:
                return

            node.next = next.next
            next.next = next.next.next
            node.next.next = next
            node = node.next
            next = node.next


sol = Solution()
a = ListNode(5)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)

sol.reverseBetween(b, 1, 2)