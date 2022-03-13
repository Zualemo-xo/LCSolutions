"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hc1=hc=head
        ans=copy=Node(-1)
        #1)create dup pointers
        while(head!=None):
            temp=head.next
            #copy
            head.next=Node(head.val)
            #head.next.random=head.random
            #moving to next actual node
            head.next.next=temp
            head=head.next.next
        #2)to dup pointers add random ll    
        while(hc1!=None):
            #copy
            hc1.next.random=None if hc1.random==None else hc1.random.next
            #moving to next actual node
            hc1=hc1.next.next
            
        #3)create new ll and restore old ll    
        while(hc!=None):
            copy.next=hc.next
            copy=copy.next
            #copy.random=hc.next.random NOT NEEDED AS I HAVE ASSIGNED copy.next=hc.next in prev step , which has all ll details
            #restore old node by removing duplicates
            hc.next=hc.next.next
            hc=hc.next
        return(ans.next)
        