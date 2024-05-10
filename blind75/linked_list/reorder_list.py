# the solution is a little bloated for a couple reasons - NC
# has exact same approach but much cleaner code: 
#
# - you don't need the halveLinkedList helper func, you can
#   find the second half in the main body, disconnect the link
#   (so you have 2 separate halves), and you still have the 
#   reference to the head for the 1st half
# - you don't need any dummy nodes
# - assignments doing the same thing for different variables
#   can be written on the same line w/ comma without sacrificing 
#   readability and making code more concise 
#   (e.g. tmp, tmp2 = firstHalf.next, reversedSecondHalf.next)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # separate into 2 halves
        # reverse 2nd half
        # merge 2 lists
        
        firstHalf, secondHalf = self.halveLinkedList(head)
        reversedSecondHalf = self.reverseLinkedList(secondHalf)
        
        dummy = ListNode()
        dummy.next = firstHalf
        
        while reversedSecondHalf:
            tmp = firstHalf.next
            tmp2 = reversedSecondHalf.next
            
            firstHalf.next = reversedSecondHalf
            reversedSecondHalf.next = tmp
            
            firstHalf = tmp
            reversedSecondHalf = tmp2
        
        return dummy.next
    
        
    def halveLinkedList(self, head):
        dummy = ListNode()
        dummy.next = head
        h1 = dummy
        h2 = dummy
        while h2 and h2.next:
            h2 = h2.next.next
            h1 = h1.next
        
        secondHalf = h1.next
        h1.next = None
        firstHalf = dummy.next
        return (firstHalf, secondHalf) 
    
    
    def reverseLinkedList(self, head):
        dummy = None
        while head:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
        return dummy
    
    
    def stringifyLinkedList(self, head):
        vals = ""
        while head:
            vals += str(head.val)
            vals += ", "
            head = head.next
        return vals