# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeDupes(lst, dupeFlag):
        if lst.next == None:
            return 
        
        if lst.next != None and lst.next.next != None:
            if lst.next.val == lst.next.next.val:
                lst.next = lst.next.next
                Solution.removeDupes(lst, 1)

        if dupeFlag == 1:
            lst.next = lst.next.next
            Solution.removeDupes(lst, 0)

        Solution.removeDupes(lst.next, 0)

    def deleteDuplicates(head):
        Solution.removeDupes(head, 0)
        return head
    
a = ListNode(5)
b = ListNode(4, a)
c = ListNode(4, b)
d = ListNode(3, c)
e = ListNode(3, d)
f = ListNode(2, e)

head = ListNode(1, f)

Solution.deleteDuplicates(head)