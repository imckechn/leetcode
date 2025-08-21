from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def getTailAndLength(self, head):
        length = 0
        while head.next:
            length += 1
            head = head.next

        return head, length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        tail, length = self.getTailAndLength(head)
        tail.next = head
        diff = length - k
        
        if k == 0:
            return head

        if k > 0:
            for i in range(k+1):
                tail = head
                head = head.next

            tail.next = None
            return head
        
        else:
            separator = head
            for i in range(diff + 1):
                separator = separator.next

            newHead = separator.next
            separator.next = None
            tail.next = head

            return newHead

                 
a = ListNode(5)
b = ListNode(4, a)
# c = ListNode(3, b)
# d = ListNode(2, c)
# e = ListNode(1, d)

sol = Solution()
sol.rotateRight(b, 0)