class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman Ford Algo MODIFIED
        dist=[float("inf") for i in range(n)]
        temp=[float("inf") for i in range(n)] #to handle k
        temp[src]=0
        dist[src]=0 #initialize source distance to 0 (start pt)
        #TEMP is needed to prevent the WRONG override cases such as TC 43 AND 44
        # IT allows for us to give priority to min stop for a given iteration , by preventing dist to be filled with wrong values, which might affect getting the final ans in LOOP2 itself
        for i in range(0,k+1):
            for u,v,wt in flights:
                if(dist[u]+wt<temp[v]): 
                    temp[v]=dist[u]+wt
            for i in range(0,len(temp)):
                dist[i]=temp[i]
            print(dist)
        #print(dist)
        return(-1 if dist[dst]==float("inf") else dist[dst])

