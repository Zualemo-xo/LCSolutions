# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l=[]
        for i in lists:
            while(i!=None):
                l.append(i.val)
                i=i.next
        #print(l)
        l=sorted(l)
        ans=n=ListNode(-1)
        for i in l:
            n.next=ListNode(i)
            n=n.next
        return(ans.next)
        
        