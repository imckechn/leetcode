# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver = False

        head = ListNode()
        current = head

        while l1 != None or l2 != None:
            if l1 and l2:
                total = l1.val + l2.val
                if carryOver:
                    total += 1
                    carryOver = False

                if total >= 10:
                    carryOver = True
                    total -= 10

                nextNode = ListNode(total)
                current.next = nextNode
                current = nextNode

                l1 = l1.next
                l2 = l2.next

            elif l1:
                total = l1.val
                if carryOver:
                    total += 1
                    carryOver = False

                if total >= 10:
                    carryOver = True
                    total -= 10

                current.next = ListNode(total)
                current = current.next
            
                l1 = l1.next

            else:
                total = l2.val
                if carryOver:
                    total += 1
                    carryOver = False

                if total >= 10:
                    carryOver = True
                    total -= 10

                current.next = ListNode(total)
                current = current.next
            
                l2 = l2.next

        if carryOver:
            current.next = ListNode(1)
        return head.next
