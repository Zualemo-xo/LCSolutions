# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans1=ans=ListNode(None)
        while(list1!=None and list2!=None):
            if(list1.val>=list2.val):
                ans.next=list2 #it dosent matter as next values are replaced
                ans=ans.next
                list2=list2.next
                
            elif(list1.val<list2.val):
                ans.next=ListNode(list1.val)
                ans=ans.next
                list1=list1.next
                
        ans.next=list1 or list2
        return(ans1.next)