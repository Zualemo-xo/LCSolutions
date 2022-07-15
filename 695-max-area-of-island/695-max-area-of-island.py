class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # TC: O(M*N) SC:O(M*N)
        def isvalid(u,v):
            if(u>=0 and v>=0 and u<len(grid) and v<len(grid[0]) and grid[u][v]!=0 and (u,v) not in visited):
                return(True)
            return(False)
        visited=set()
        def dfs(r,c):
            x=[0,0,1,-1]
            y=[1,-1,0,0]
            
            # if((r,c) in visited):
            #     return(0)
            #else:
            visited.add((r,c))
            tmp=0
            for i in range(4):
                if(isvalid(r+x[i],c+y[i])):
                    tmp=tmp+1+dfs(r+x[i],c+y[i])
            return(tmp)

        
        ans=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if((i,j) not in visited and isvalid(i,j)):
                    #print(i,j)
                    
                    tans=dfs(i,j)+1 #   To accomodate for the curr element
                    #print(visited)
                    ans=max(ans,tans)
                    #print(ans)
        return(ans)
                    
        