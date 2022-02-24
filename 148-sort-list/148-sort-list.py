# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        l.sort()
        ans=n=ListNode(-1)
        for i in l:
            ans.next=ListNode(i)
            ans=ans.next
        return(n.next)
        
        