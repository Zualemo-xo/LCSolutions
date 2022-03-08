# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        sp=fp=head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next
            if(sp==fp):
                return(True)
        return(False)