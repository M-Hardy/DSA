# *implement recursive solution for practice later

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = None
        
        while head:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
            
        return dummy
    