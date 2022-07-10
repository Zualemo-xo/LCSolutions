class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Memization TC: O(N) SC:O(N)
        n=len(cost)
        self.memo=[-1 for i in range(n+1)]
        def dp(pos):
            if(pos>=n):
                return(0)
            if(self.memo[pos]!=-1):
                return(self.memo[pos])
            x=cost[pos]+min(dp(pos+1),dp(pos+2))
            self.memo[pos]=x
            return(x)
        
        ans=min(dp(0),dp(1))
        return(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    