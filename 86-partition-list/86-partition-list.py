# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        l=[]
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        
        lesser=[]
        
        for i in range(0,len(l)):
            if(l[i]<x):
                lesser.append(l[i])
                l[i]=float("-inf")
        
        ans=lesser+l
        pos=0
        temp=head
        while(temp!=None):
            #print(temp)
            if(ans[pos]==float("-inf")):
                pos+=1
                continue
            temp.val=ans[pos]
            temp=temp.next
            pos+=1
        return(head)