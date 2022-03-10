# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #if ll  equal or not
        t1,t2=l1,l2
        cnt1,cnt2=0,0
        while(t1!=None or t2!=None):
            if(t1==None):
                t2=t2.next
                cnt1+=1
                continue
            if(t2==None):
                t1=t1.next
                cnt2+=1
                continue
            #print(t1.val,t2.val)
            t1=t1.next
            t2=t2.next
        #print(cnt1,cnt2)
        #adding leading zeroes 
        a1=t1=ListNode(-1)
        a2=t2=ListNode(-1)
        while(cnt1!=0 or cnt2!=0):
            if(cnt1!=0):
                t1.next=ListNode(0)
                t1=t1.next
                cnt1-=1
            if(cnt2!=0):
                t2.next=ListNode(0)
                t2=t2.next
                cnt2-=1
                #print(cnt2,t2)
                
        t1.next=l1
        #print(a2)
        t2.next=l2
        #print(a2)
        l1,l2=a1.next,a2.next
        #print("++++++++++",l1,"______",l2)
        #addition
        carry=0
        ans=l2
        # Recursion to calculate the sum 
        def helper(l1,l2):
            if(l1.next==None):
                x=(l2.val+l1.val)%10
                carry=(l1.val+l2.val)//10
                l2.val=x
                return(carry)
            else:
                carry=helper(l1.next,l2.next)
                x=(l2.val+l1.val+carry)%10
                carry=(l1.val+l2.val+carry)//10
                l2.val=x
                return(carry)
        carry=helper(l1,l2) #final carry rtetuened
        answer=ans=ListNode(-1) 
        if(carry!=0): # add carry to start of LL if exists
            ans.next=ListNode(carry)
            ans=ans.next
        ans.next=l2
        return(answer.next)