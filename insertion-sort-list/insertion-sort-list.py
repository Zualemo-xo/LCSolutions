# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1=head
        while(l1!=None):
            l2=l1.next
            while(l2!=None):
                if(l2.val<l1.val):
                    l1.val,l2.val=l2.val,l1.val
                l2=l2.next
            l1=l1.next
                    
        return(head)
        