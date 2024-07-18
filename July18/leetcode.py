# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def append(l3, sum):   
    if (sum > 100):
        l3.val = 1
        l3.next = ListNode()
    
    if (sum > 10):
        l3.val = sum / 10
        l3.next = ListNode()

    l3.val = sum % 10
    l3.next = ListNode()

    return l3.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        output = ListNode()
        og = output

        output = append(output, l1.val + l2.val)
        
        currentL1 = l1
        currentL2 = l2

        while(currentL1.next and currentL2.next):
            currentL1 = currentL1.next
            currentL2 = currentL2.next

            output = append(output, l1.val + l2.val)

        if (currentL1.next):
            currentL1 = currentL1.next

            output = append(output, l1.val + l2.val)

        elif (currentL2.next):
            currentL2 = currentL2.next

            output = append(output, l1.val + l2.val)

        return og

append(ListNode(), 7)


        