class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Union Find & find no of connected components
        adj=set()
        graph=[]
        cnt=0
        #Convert into a graph with nodes
        for i in range(0,len(grid)):
            tmp=[]
            for j in range(0,len(grid[i])):
                if(grid[i][j]=="1"):
                    tmp.append(cnt)
                    cnt+=1
                else:
                    tmp.append(-1)
                
            graph.append(tmp)
        #print(graph)
        
        #Create adj list
        def isvalid(r,c):
            if(r>=0 and r<len(graph) and c>=0 and c<len(graph[0]) and graph[r][c]!=-1):
                return(True)
            return(False)
        
        xnew=[0,0,-1,1]
        ynew=[-1,1,0,0]
        for i in range(0,len(graph)):
            for j in range(0,len(graph[i])):
                if(graph[i][j]!=-1):
                    for k in range(0,4):
                        if(isvalid(i+xnew[k],j+ynew[k])):
                            #convert to a directed graph for ease of using union find
                            x1=min(graph[i][j],graph[i+xnew[k]][j+ynew[k]])
                            x2=max(graph[i][j],graph[i+xnew[k]][j+ynew[k]])
                            adj.add( ( x1,x2  ) )
        print(adj)
        
        #Apply union find to newly created adj list
        
        self.parent=defaultdict(int)
        self.cnt=0 
        def initialize(n):
            for i in range(n):
                self.parent[i]=i
               
        def getAbsoluteParent(u):
            if(u!=self.parent[u]):
                self.parent[u]=getAbsoluteParent(self.parent[u])
                return(self.parent[u])
            return(u)
        
        def union(u,v):
            AbsoluteParentu=getAbsoluteParent(u)
            AbsoluteParentv=getAbsoluteParent(v)
            #Assign based on bigger union
            if(AbsoluteParentu!=AbsoluteParentv):
                self.parent[AbsoluteParentv]=AbsoluteParentu

        
        initialize(cnt)
        adj=list(adj)
        adj.sort()
        for u,v in adj:
            union(u,v)
            #print(u,v)
            #print(self.parent)
        
        #Find unique parents inside the parent array
        #print(self.parent)
        #return( len(set(self.parent.values())) )
        ans=set()
        for i in self.parent:
            ans.add(getAbsoluteParent(self.parent[i]))
            
        return(len(ans))
        
                
                        
                
                
                
        