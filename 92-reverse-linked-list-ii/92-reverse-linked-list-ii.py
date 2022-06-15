# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        #Recursion
        curr=head
        cnt=0
        def recursion(swapvalue,curr,cnt,right):
            while(curr!=None):
                cnt+=1
                if(cnt==right):
                    temp=curr.val
                    curr.val=swapvalue
                    return(temp)
                else:
                    curr=curr.next
        
        while(curr!=None):
                cnt+=1
                if(cnt<left):
                    curr=curr.next
                
                elif(cnt>=left and cnt<=(left+right)/2): #perform recursive swapping for half of the linked list , the 2nd half will be automatically sorted
                    curr.val=recursion(curr.val,curr,cnt-1,right+left-cnt)
                    curr=curr.next
                else:
                    curr=curr.next
        return(head)
        

            