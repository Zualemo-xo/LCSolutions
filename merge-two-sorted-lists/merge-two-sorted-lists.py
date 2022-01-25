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
        ans=ListNode(None)
        ans1=ans
        print(ans)
        while(list1!=None and list2!=None):
            print(list1.val,list2.val)
            print(ans)
            if(list1.val>=list2.val):
                ans.next=ListNode(list2.val)
                ans=ans.next
                list2=list2.next
                
            elif(list1.val<list2.val):
                ans.next=ListNode(list1.val)
                ans=ans.next
                list1=list1.next
                
        while(list1!=None):
            ans.next=ListNode(list1.val)
            ans=ans.next
            list1=list1.next
            
        while(list2!=None):
            ans.next=ListNode(list2.val)
            ans=ans.next
            list2=list2.next
        return(ans1.next)