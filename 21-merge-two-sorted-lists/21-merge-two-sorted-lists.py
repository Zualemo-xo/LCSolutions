# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            #print("L1:",l1)
            l1.next = self.mergeTwoLists(l1.next, l2)
            #print("L1 AFTER:",l1)
            return l1
        else:
            #print("L2:",l2)
            l2.next = self.mergeTwoLists(l1, l2.next)
            #print("L2 AFTER:",l2)
            return l2