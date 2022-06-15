# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # TC O(2N) SC 0(K) K=RIGHT-LEFT
        stack=deque()
        temp=head
        cnt=0
        while(temp!=None):
            cnt+=1
            if(cnt>=left and cnt<=right):
                stack.append(temp.val)
            temp=temp.next
        temp=head
        cnt=0
        while(temp!=None):
            cnt+=1
            if(cnt>=left and cnt<=right):
                temp.val=stack.pop()
            temp=temp.next
        return(head)