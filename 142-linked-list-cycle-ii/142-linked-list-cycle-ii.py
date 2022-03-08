# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp=fp=newp=head
        #detect cycle
        while(True):
            if(fp==None or fp.next==None):
                return(None)
            sp=sp.next
            fp=fp.next.next
            if(sp==fp):
                break
        #find point by initializing a newpointer frmstart and continuing sp interation
        while(newp!=sp):
            newp=newp.next
            sp=sp.next
        return(newp)