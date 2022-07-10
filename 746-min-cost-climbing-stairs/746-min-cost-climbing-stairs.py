class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Botom Up Soace Optimized TC: O(N) SC:O(1)
        n=len(cost)
        dp=[0 for i in range(2)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i%2]=cost[i]+min(dp[(i-1)%2],dp[(i-2)%2])
            

        ans=min(dp[i%2],dp[(i-1)%2])
        return(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    