class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=defaultdict(bool)
        #Start BFS AT A POINT WHICH HAS MOST CONNECTIONS
        maxl,startpoint=0,0
        for pt,i in enumerate(graph):
            if(len(i)>maxl):
                startpoint=pt
                maxl=len(i)
                #print(pt,i)
        #print(maxl,pt)
        color[startpoint]=True #key :value here are node:color 1 (True) or 2 (False)
        
        #BFS
        queue=deque([startpoint])
        visited=set()
        while(len(queue)!=0):
        #for node in range(0,len(graph)):--iteration of all nodes in order instead of BFS
            node=queue.popleft()
            #print(node)
            for neighbor in graph[node]:
                if(neighbor not in color):
                    color[neighbor]=not color[node] #different color to original node
                    queue.append(neighbor)
                    
                elif(color[neighbor]==color[node]): #when neighbor also has same color coordinate, it means graph is !bipartite
                    return(False)
                
        
        return(True)
                