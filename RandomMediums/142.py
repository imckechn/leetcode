# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        visited = [head]
        current = head
       
        while True:
            if current.next == None:
                return None
            
            else:
                current = current.next
                if current.val in visited:
                    return current
                
                else:
                    visited.append(current)

        
a = ListNode(-1)
b = ListNode(-7)
c = ListNode(7)
d = ListNode(-4)
e = ListNode(19)
f = ListNode(6)
g = ListNode(-9)
h = ListNode(-5)
i = ListNode(-2)
j = ListNode(-5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j

print(Solution.detectCycle(None, a).val)