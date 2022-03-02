class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bott0m up
        if(len(cost)==2):
            return(min(cost))
        l=[]
        l.append(cost[0])
        l.append(cost[1])
        for i in range(2,len(cost)):
            l.append(cost[i]+min(l[i-1],l[i-2]))
        return(min(l[-1],l[-2]))
            