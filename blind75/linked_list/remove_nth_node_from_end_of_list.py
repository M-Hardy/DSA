# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode()
        dummy.next = head
        
        first = dummy
        second = dummy
        
        while n:
            first = first.next
            n -= 1
        
        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next