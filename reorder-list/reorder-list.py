# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        start,startf=head,head
        arr=[]
        while(start!=None):
            arr.append(start.val)
            start=start.next
        #print(arr)
        L,R=0,len(arr)-1
        cnt=0
        while(startf!=None):
            if(cnt%2==0):
                startf.val=arr[L]
                L+=1
            else:
                startf.val=arr[R]
                R-=1
            startf=startf.next
            cnt+=1
            
        
        