# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(k==0 or head==None):
            return(head)
        cnt=0
        temp=head
        while(temp!=None):
            temp=temp.next
            cnt+=1
        k%=cnt
        while(k>0):
            k-=1
            prev=ListNode(-1)
            prev.next=head
            temp=head
            while(temp!=None):
                if(temp.next==None): #break last node and make it head
                    prev.next=None
                    temp.next=head
                    head=temp
                    break
                temp=temp.next
                prev=prev.next
        return(head)