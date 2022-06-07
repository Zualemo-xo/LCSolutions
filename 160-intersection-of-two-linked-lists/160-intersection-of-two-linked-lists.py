# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1,head2,flag=headA,headB,0
        while(True):
            if(flag>=3):
                return(None)
            if(head1==None):
                head1=headB
                flag+=1
            if(head2==None):
                head2=headA
                flag+=1
            elif(head1==head2):
                return(head1)
            else:
                head1=head1.next
                head2=head2.next
