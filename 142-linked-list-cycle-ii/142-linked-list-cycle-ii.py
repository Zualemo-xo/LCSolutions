# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #print(head)
        l={}
        while(head):
            if(head not in l):
                l[head]=head
            #print(head.val)
            else:
                return(head)
            head=head.next