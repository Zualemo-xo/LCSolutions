# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.l=[]
        while(head!=None):
            self.l.append(head.val)
            head=head.next

    def getRandom(self):
        """
        :rtype: int
        """
        x=random.randrange(0,len(self.l))
        return(self.l[x])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()