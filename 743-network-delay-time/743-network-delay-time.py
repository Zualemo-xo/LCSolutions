class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Bellman Ford WITH LIST BASED DIST MATRIX
        dist=[float("inf") for i in range(0,n)]
        dist[k-1]=0
        for i in range(n-1): #ITERATE N-1 TIMES
            for u,v,wt in times:
                if(dist[u-1]+wt<dist[v-1]):
                    dist[v-1]=dist[u-1]+wt

        #Node is to reachable/Not connected
        if(max(dist)==float("inf")):
            return(-1)
        else:
            return(max(dist))
            return(max(dist.values()))