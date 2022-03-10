# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1,t2=l1,l2
        greater=2
        carry=0
        while(t1!=None or t2!=None):
            
            if(t1==None):
                greater=2
                x=(t2.val+carry)%10
                carry=(t2.val+carry)//10
                t2.val=x
                if(carry!=0 and t2.next==None):
                    t2.next=ListNode(carry)
                    t2=t2.next
                #t2.next=ListNode(carry)
                t2=t2.next
                continue
            if(t2==None):
                greater=1
                x=(t1.val+carry)%10
                carry=(t1.val+carry)//10
                t1.val=x
                if(carry!=0 and t1.next==None): #add carry at last if ll has ended
                    t1.next=ListNode(carry)
                    t1=t1.next
                t1=t1.next
                continue
            else:
                x=(t2.val+t1.val+carry)%10
                carry=(t1.val+t2.val+carry)//10
                t2.val=t1.val=x
                #print(l1.val+l2.val+carry,carry)
                if(carry!=0 and t1.next==None and t2.next==None): #add carry at last if ll has ended
                    t2.next=ListNode(carry)
                    t2=t2.next
                t2=t2.next
                t1=t1.next
                
        if(greater==1):
            return(l1)
        else:
            return(l2)

        