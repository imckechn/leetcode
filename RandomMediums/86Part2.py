from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        copy = head
        next, outOfPlaceFirst = Solution.collectFirstSection(copy, x)
        next, outOfPlaceMiddleLessThan, outOfPlaceMiddleLargerThan = Solution.collectMiddle(next, x)
        outOfPlaceLast = Solution.collectFinal(next, x)

        return Solution.reassembleList(head, x, outOfPlaceFirst, outOfPlaceMiddleLessThan, outOfPlaceMiddleLargerThan, outOfPlaceLast)
    
    # Go to the first x, pull out all numbers less than x and store them in order in a list
    # Return 
    def collectFirstSection(list, x):
        outOfPlace = None
        while (list.val != x):
            next = None
            if list.val > x:
                next = list.next
                outOfPlace = Solution.appendNodeToList(list, outOfPlace)
                list = next

            else:
                list = list.next

        return list, outOfPlace

    def collectMiddle(list, x):
        count = Solution.countX(list, x)

        if count == 1:
            return list.next, None, None
        else:
            found = 1
            list = list.next

            lessThan = None
            greaterThan = None

            while found != count:
                if list.val == x:
                    found += 1
                    list = list.next
                    continue

                if list.val < x:
                    lessThan, list = Solution.appendNodeToList(list, lessThan)

                else:
                    greaterThan, list = Solution.appendNodeToList(list, greaterThan)       

            return list, lessThan, greaterThan

    def countX(list, x):
        count = 1
        while list.next != None:
            list = list.next

            if list.val == x:
                count += 1

        return count

    def appendNodeToList(node, list):
        if list == None:
            list = node
            node = node.next
            list.next = None
            return list, node
        
        else:
            head = list
            while(list.next != None):
                list = list.next

            list.next = node

        node = next
        return head

    def collectFinal(list, x):
        outOfPlace = None
        while (list != None):
            next = None
            if list.val < x:
                next = list.next
                outOfPlace = Solution.appendNodeToList(list, outOfPlace)
                list = next

            else:
                list = list.next

        return outOfPlace

    def reassembleList(list, x, a, b, c, d):
        head = list

        while list.next.val != x:
            list = list.next

        next = list.next
        list.next = b

        while list.next != None:
            list = list.next

        list.next = d

        while list.next != None:
            list = list.next

        list.next = next

        while list.next.val == x:
            list = list.next

        next = list.next

        list.next = a
        while list.next != None:
            list = list.next

        list.next = c
        while list.next != None:
            list = list.next

        list.next = next

        return head


a = ListNode(2)
b = ListNode(5, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(3, d)
f = ListNode(4, e)
g = ListNode(1, f)

Solution.partition(None, g, 3)
