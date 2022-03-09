# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return(head)
        prev=head
        curr=head.next
        d=defaultdict(int)
        d[prev.val]+=1
        #make list into unique
        while(curr!=None):
            # print(d)
            # print()
            if(curr.val in d):
                d[curr.val]+=1
                prev.next=curr.next
            else:
                d[curr.val]+=1
                prev=prev.next
            curr=curr.next
            
        #remove first ele if it ha repetition
        prev=head
        while(prev!=None):
            if(d[prev.val]>1):
                prev=prev.next
            else:
                break
        if(prev==None):
            return(prev)
        head=prev
        curr=head.next
        #remove other mid ele if it has repetition
        while(curr!=None):

            if(d[curr.val]>1):
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        return(head)
                