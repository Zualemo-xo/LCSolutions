class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=deque([[0,0,0]])
        visited=set()
        n,m=len(grid),len(grid[0])
        
        #ans=float("inf")
        
        while(len(queue)!=0):
            curr=queue.popleft()
            #print(curr)
            i,j,dist=curr[0],curr[1],curr[2]
            
            if(i==n-1 and j==m-1 and grid[i][j]!=1): #FINAL ANS
                return(dist+1)
            
            if((i,j) in visited):
                continue
            visited.add((i,j))
            if(grid[i][j]==1): #Invalid path
                continue
            
            else: #Look around and add possible connections
                #8 cases
                if(i-1>=0 and j-1>=0 and (i-1,j-1) not in visited):
                    queue.append([i-1,j-1,dist+1])
                if(i-1>=0 and j>=0 and (i-1,j) not in visited):
                    queue.append([i-1,j,dist+1])
                if(i-1>=0 and j+1<=m-1 and (i-1,j+1) not in visited):
                    queue.append([i-1,j+1,dist+1])
                
                if(i>=0 and j-1>=0 and (i,j-1) not in visited):
                    queue.append([i,j-1,dist+1])   
                if(i>=0 and j+1<=m-1 and (i,j+1) not in visited):
                    queue.append([i,j+1,dist+1])
                    
                if(i+1<=n-1 and j-1>=0 and (i+1,j-1) not in visited):
                    queue.append([i+1,j-1,dist+1])
                if(i+1<=n-1 and j>=0 and (i+1,j) not in visited):
                    queue.append([i+1,j,dist+1])
                if(i+1<=n-1 and j+1<=m-1 and (i+1,j+1) not in visited):
                    queue.append([i+1,j+1,dist+1])
        
        return(-1)  #BOTTOM-right was never reached and queue became empty
                