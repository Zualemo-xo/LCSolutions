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
        if(k==0):
            return(head)
        #optimizing to O(n) from O(n*k)
        temp=head
        c=0
        while(temp!=None):
            c+=1
            print(c)
            if(c==cnt-k):
                t=rot=temp.next
                temp.next=None
                while(t.next!=None): #break cnt-k-1 node and make it head
                    t=t.next
                #at the last node connect to head
                t.next=head
                head=rot
            temp=temp.next
        return(head)