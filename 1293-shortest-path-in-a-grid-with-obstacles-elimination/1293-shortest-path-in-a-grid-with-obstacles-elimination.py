class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        #USE BFS WITH CNT
        def isvalid(x,y,k,step):
            if(x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and k>=0):
                return(True)
            return(False)
            
        #(Xcoord,Ycoord,Kremaining,steps)
        queue=deque([(0,0,k,0)])
        visited=set()
        x=[0,1,-1,0]
        y=[1,0,0,-1]
        m,n=len(grid),len(grid[0])
        while(len(queue)!=0):
            coord=queue.popleft()
            pts=(coord[0],coord[1],coord[2]) # k is needed as at a future iteration , it might arrive with a higher k
            while(pts not in visited):
                visited.add(pts)
                if((coord[0],coord[1])==(m-1,n-1)):
                    #print(coord[3])
                    return(coord[3]) #steps
                
                for i in range(4):
                    newx=coord[0]+x[i]
                    newy=coord[1]+y[i]
                    if(isvalid(newx,newy,coord[2],coord[3])):
                        if(grid[newx][newy]==1):
                            queue.append((newx,newy,coord[2]-1,coord[3]+1))
                        else: #no obstacles
                            queue.append((newx,newy,coord[2],coord[3]+1))
            
            
        return(-1)
        
        