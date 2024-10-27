# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(head, left, right):
        newList = None
        finalNode =  head
        cur = head

        while True:
            if cur.val == left:
                finalNode = head.next 
                newList = cur
            
            else:
                copy = cur
                copy.next = newList
                newList = copy                

                if newList.val == right:
                    finalNode.next = newList
                    newList.next = cur.next
                    break
            cur = cur.next

        return head


a = ListNode(5)
b = ListNode(4, a)
c = ListNode(3, b)
d = ListNode(2, c)
head = ListNode(1, d)

print(Solution.reverseBetween(head, 2, 4).val)
