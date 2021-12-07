# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans=0
        ptr=head
        cnt=-1 #to get n-1
        while(ptr!=None):
            cnt+=1 
            ptr=ptr.next
        while(head!=None):
            ans=ans+head.val*(2**cnt)
            cnt-=1
            head=head.next
        return(ans)