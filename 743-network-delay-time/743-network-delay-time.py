import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # Dijkstra
        
        #Create adjacency matrix [n+1--- 1 to n range ]
        adj=[[-1 for i in range(n+1)] for j in range(n+1)] # DONT INITIALIZE AS 0 , O CAN BE AN ACTUAL DISTANCE VALUE
        #dij=[[float('inf') for i in range(n+1)] for j in range(n+1)]
        visited=[]
        #print(adj)
        for node in times:
            #print(node)
            adj[node[0]][node[1]]=node[2]
        print(adj)
        # Create priority queue
        l=[(0,k)]
        heapq.heapify(l)
        visited=defaultdict(int)
        
        for i in range(1,n+1):
            visited[i]=float("inf")
            
        while(len(l)!=0):
            lent,ele=heapq.heappop(l)
            #print(ele,lent)
            #visited[ele]=min(lent,visited[ele])
            
            if(lent<visited[ele]):
                visited[ele]=lent
            #Add newfound connected nodes of 'ele' into 'l'
                for j in range(1,len(adj[ele])):    
                    if(adj[ele][j]!=-1):
                        heapq.heappush(l,(lent+adj[ele][j],j)) # push into PQ new connections which are found
            #print(l)
        #print(visited)
        ans=max(visited.values())
        if(ans!=float("inf")):
            #print(visited)
            return(max(visited.values()))
        else:
            return(-1)
        
        