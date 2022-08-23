# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        return(True if l==l[::-1] else False)
            