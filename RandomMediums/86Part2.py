from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerList = ListNode()
        largerList = ListNode()
        xValues = ListNode()

        smallerListHead = smallerList
        largerListHead = largerList

        while (head != None):
            if head.val < x:
                smallerList.next = head
                smallerList = smallerList.next
            
            elif head.val >= x:
                largerList.next = head
                largerList = largerList.next

            head = head.next

        smallerList.next = None
        largerList.next = None
        xValues.next = None

        head = smallerListHead.next

        if head == None:
            return largerListHead.next

        while smallerListHead.next != None:
            smallerListHead = smallerListHead.next

        smallerListHead.next = largerListHead.next

        return head
    
    

a = ListNode(2)
b = ListNode(5, a)
c = ListNode(2, b)
d = ListNode(3, c)
f = ListNode(4, d)
g = ListNode(1, f)

n = ListNode(1)

Solution.partition(None, n, 0)
