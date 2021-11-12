# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if(head==None):
        #     return(head)
        while(head!=None and head.val==val):
            head=head.next

        curr=head
        while(curr!=None):
            if(curr.next!=None and curr.next.val==val):
                curr.next=curr.next.next
            else:
                curr=curr.next

        return(head)
        