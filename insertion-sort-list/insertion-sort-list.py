
class Solution(object):
    def insertionSortList(self, head):
        #INSERTION SORT BY SWAPPING NODE'S VALUE
        l1=head
        while(l1!=None):
            l2=head
            #curr=l1.val
            while(l2!=l1):
                if(l2.val>l1.val):
                    l1.val,l2.val=l2.val,l1.val
                
                l2=l2.next
            l1=l1.next
                    
        return(head)
        