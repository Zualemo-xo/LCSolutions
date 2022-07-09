
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Using Monotonic Queue TC: O(N) SC: O(N)
        q=deque( [0] ) #Monotonic queue stored in lowest to highest index
        dp=[nums[0]] #Storing final answer
        
        for i in range(1,len(nums)):
            #print(q,dp)
            cnt=0
            while(q[cnt]<i-k): #pop all elements not falling within the range
                ele=q.popleft()
                
            dp.append( dp[q[0]]+nums[i] )
            #pop indices which won't be ever chosen in the future, as our new dp is greater than those old dp elements
            while(len(q)!=0 and dp[q[-1]] <= dp[-1]):
                q.pop()
            q.append( i )
            
        #print(q,dp)
        return(dp[-1])