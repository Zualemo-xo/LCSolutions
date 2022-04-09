# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        cp=[]
        cnt,mindist=0,float("inf")
        prev=head
        head=head.next
        while(head.next!=None):
            if((prev.val>head.val and head.next.val>head.val) or (prev.val<head.val and head.next.val<head.val)):
                mindist=float("inf") if len(cp)==0 else min(mindist,cnt-cp[-1]) #calc and compare mindist whenever new CPt is found
                cp.append(cnt)
            cnt+=1
            prev=prev.next
            head=head.next
            
        if(len(cp)<2):
            return([-1,-1])
        else:
            return([mindist,cp[-1]-cp[0]])
        #print(cp)