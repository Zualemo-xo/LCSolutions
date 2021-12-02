# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None):
            return(head)
        odd=head
        startodd=odd
        
        even=head.next
        starteven=even
        
        while(even!=None and even.next!=None and odd.next!=None and odd!=None):
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=starteven
        return(startodd)
   