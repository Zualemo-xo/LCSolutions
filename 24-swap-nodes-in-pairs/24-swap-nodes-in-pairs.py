# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helper(self,prev,head):
        if(head==None or head.next==None):
            return()
        prev.next=head.next
        temp=head.next
        head.next=head.next.next
        temp.next=head
        #print(head)
        self.helper(prev.next.next,head.next)
        
        #return(head)
        
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n=ListNode(-1) # to accomodate for prev
        n.next=head
        self.helper(n,n.next)
        #print(n)
        return(n.next)
        