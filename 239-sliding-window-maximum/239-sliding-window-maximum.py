from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #maxn=-1
        #pos=-1
        q=deque()
        ans=[]
        for i,cur in enumerate(nums):
            while(len(q)!=0 and nums[q[-1]]<cur):
                q.pop()
            q.append(i) #append indices
            
            if(q[0]==i-k): #if beyond left bound, pop that ele
                q.popleft()
            
            if(i>=k-1): # when initial threshold of k-window is reached , start adding answers --drew and see
                ans.append(nums[q[0]])
        
        return(ans)
            