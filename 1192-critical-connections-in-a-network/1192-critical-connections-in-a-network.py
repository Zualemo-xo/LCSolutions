class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # Find Bridges in a graph
        adj=defaultdict(list)
        
        def create_adj():
            for u,v in connections:
                adj[u].append(v)
                adj[v].append(u) # Undirected graph
        
        
        low=[float("inf")]*n
        discovery=[float("inf")]*n
        visited=[False]*n
        parent=[-1]*n
        self.time=0
        ans=[]
        
        def bridge_dfs(node):
            self.time+=1
            visited[node]=True
            discovery[node]=self.time
            low[node]=self.time
            #visit all adjacent nodes
            for adj_node in adj[node]:
                if(visited[adj_node]==False):
                    parent[adj_node]=node
                    bridge_dfs(adj_node)
                    
                    low[node]=min(low[node],low[adj_node]) #determine of its connected ancestor has a lesser low time
                    
                    #bridge condition
                    if(low[adj_node]>discovery[node]): # if low of child node is less than disc of parent /current node
                        ans.append([node,adj_node])
                        
                elif(adj_node != parent[node]): #Here is where the comparison between visited parent disc time and current child low time is done
                    low[node]=min(low[node],discovery[adj_node])
                    
        create_adj()
        for i in range(0,n):
            if(visited[i]==False):
                bridge_dfs(i)
        #print(parent,low,discovery)
        return(ans)
        
        
        
        