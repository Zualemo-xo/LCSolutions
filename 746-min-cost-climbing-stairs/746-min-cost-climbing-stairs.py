class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bott0m up memory optimized
        if(len(cost)==2):
            return(min(cost))
        x1=cost[0]
        x2=cost[1]
        for i in range(2,len(cost)):
            temp=x2
            x2=cost[i]+min(x1,x2)
            x1=temp
        return(min(x1,x2))
            