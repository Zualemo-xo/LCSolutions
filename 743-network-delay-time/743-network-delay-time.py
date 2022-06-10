class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Bellman Ford
        #Initialize distance matrix with inf , except for k , which  has 0 .
        dist=defaultdict(int)
        for i in range(1,n+1):
            dist[i]=float("inf")
        dist[k]=0
        
        for i in range(n-1): #ITERATE N-1 TIMES
            for u,v,wt in times:
                if(dist[u]+wt<dist[v]):
                    dist[v]=dist[u]+wt
        #print(dist)
        if(max(dist.values())==float("inf")): #Node is to reachable/Not connected
            return(-1)
        else:
            return(max(dist.values()))