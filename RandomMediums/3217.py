# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        numbers = {num:True for num in nums}

        head = ListNode(0, head)
        current = head

        while current.next != None:
            if current.next.val in numbers:
                current.next = current.next.next
            else:
                current = current.next

        return head.next
