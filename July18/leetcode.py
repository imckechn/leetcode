# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createll(arr):
    initNode = ListNode()

    initNode.val = arr[0]
    node = initNode
    index = 1
    while len(arr) > index:
        node.next = ListNode()
        node = node.next
        node.val = arr[index]
        index += 1

    return initNode


def nextNode(node):
    if node.next != None:
        return node.next
    else:
        node.next = ListNode()
        return node.next


def append(l3, sum):
    copy = l3
    
    if (sum >= 10):
        followingNode = nextNode(l3)
        followingNode.val += int(sum / 10)

    l3.val += sum % 10

    if l3.next == None:
        l3.next = ListNode()

    return copy.next

def deleteFinalNode(node):
    copy = node
    while True:
        if (copy.next.val == 0 and not copy.next.next):
            copy.next = None
            break
        else:
            copy = copy.next


class Solution:
    def addTwoNumbers(l1, l2):
        currNode = ListNode()
        og = currNode

        currNode = append(currNode, l1.val + l2.val)
        
        currentL1 = l1
        currentL2 = l2

        while (currentL1.next and currentL2.next):
            currentL1 = currentL1.next
            currentL2 = currentL2.next

            currNode = append(currNode, currentL1.val + currentL2.val)

        while (currentL1.next):
            currentL1 = currentL1.next
            currNode = append(currNode, currentL1.val)

        while (currentL2.next):
            currentL2 = currentL1.next
            currNode = append(currNode, currentL2.val)

        deleteFinalNode(og)
        return og

first = createll([2,4,3])
second = createll([5,6,4])

# first = createll([9,4,3])
# second = createll([2,6,4])
# answer = 118

Solution.addTwoNumbers(first, second)
        