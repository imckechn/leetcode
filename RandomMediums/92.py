from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        copy = head

        while copy.next != None and copy.next.val != left:
            copy = copy.next

        if copy.next != None:
            copy.next = Solution.reverseLinkedList(copy.next, right)

        return head


    def reverseLinkedList(copy, right):
        first = copy.next
        if first.next == None:
            first.next = copy
            copy.next = None

            return first
        
        second = first.next

        copy.next, first.next = first.next, copy
        copy = first
        first = copy.next

        while second != None and copy.val != right:
            first.next = second.next
            second.next = copy

            copy = second
            second = first.next

        return copy
            





a = ListNode(5)
b = ListNode(3, a)

Solution.reverseBetween(None, b, 1, 2)


# a = ListNode(6)
# b = ListNode(5, a)
# c = ListNode(4, b)
# d = ListNode(3, c)
# f = ListNode(2, d)
# g = ListNode(1, f)

# Solution.reverseBetween(None, g, 2, 5)