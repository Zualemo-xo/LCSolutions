# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp=head
        l=[]
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        print(len(l),len(l)-k+1)
        l[k-1],l[len(l)-k]=l[len(l)-k],l[k-1]
        temp=head
        for i in l:
            temp.val=i
            temp=temp.next
        return(head)
