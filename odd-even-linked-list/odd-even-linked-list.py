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
        #BFORCE WITH AUXILARRY ARRAY
        if(head==None):
            return(head)
        ansllist=ListNode(-1)
        itr=head
        l=[]
        while(itr):
            l.append(itr.val)
            itr=itr.next
        itr=ansllist
        for i in range(0,len(l),2):
            itr.next=ListNode(l[i])
            itr=itr.next
        for i in range(1,len(l),2):
            itr.next=ListNode(l[i])
            itr=itr.next
        return(ansllist.next)