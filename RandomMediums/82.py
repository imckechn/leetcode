# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        head = Solution.LinkedListBubbleSort(head)
        head = Solution.removeDupes(head)


    def removeDupes(head):
        newHead = ListNode(None, head)
        prev = newHead
        current = head
        
        while(current != None and current.next != None):
            if current.val == current.next.val:
                if current.next.next != None and current.next.val == current.next.next.val:
                    current = Solution.removeNextNode(current)

                else:
                    prev = Solution.removeNextNode(prev)
                    prev = Solution.removeNextNode(prev)
                    current = prev.next
            
            else:
                prev = current
                current = current.next

        return newHead.next
                

        
    def removeNextNode(node):
        node.next = node.next.next
        return node
    

    def LinkedListBubbleSort(head):
        changes = True

        while (changes):
            changes = False
            current = head
            while (current.next != None):
                if current.val > current.next.val:
                    current.val, current.next.val = current.next.val, current.val
                    changes = True

                current = current.next

        return head

a = ListNode(1)
b = ListNode(1, a)
c = ListNode(4, b)
d = ListNode(3, c)
e = ListNode(3, d)
f = ListNode(2, e)
g = ListNode(4, f)

Solution.deleteDuplicates(None, g)
