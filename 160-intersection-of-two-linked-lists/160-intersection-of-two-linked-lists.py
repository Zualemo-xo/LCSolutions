# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1,head2,flag=headA,headB,0
        while(head1!=head2):
            if(head1==None):
                head1=headB
            else:
                head1=head1.next
            if(head2==None):
                head2=headA
            else:
                head2=head2.next
        return(head1)
