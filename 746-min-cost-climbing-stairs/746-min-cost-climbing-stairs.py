class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Botom Up TC: O(N) SC:O(N)
        n=len(cost)
        dp=[0 for i in range(n)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
            

        ans=min(dp[i],dp[i-1])
        return(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    