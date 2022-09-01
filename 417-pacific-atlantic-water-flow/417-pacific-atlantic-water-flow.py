class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.ans=[]
        #memo heights heights[i]
        self.memo=[[float("inf") for i in range(0,len(heights[0]))] for j in range(0,len(heights))]
        def isvalid(r,c,x,y):
            #print(r,c,x,y)
            if(x<0 or y<0):
                return(-1) #pacific
            elif(x>=len(heights) or y>=len(heights[0])):
                return(-2) #atlantic
            elif(heights[r][c]<heights[x][y]):
                return(0) # new point has higher height
            else:
                return(1)
        
        def bfs(r,c):
            queue=deque([[r,c]])
            x=[-1,1,0,0]
            y=[0,0,-1,1]
            pacific=False
            atlantic=False
            visited=set((r,c))
            while(len(queue)!=0):
                #print(queue)
                #mEOMIZATION
                ele=queue.popleft()
                #visited.add((ele[0],ele[1]))
                val=self.memo[ele[0]][ele[1]]
                if(val!=float("inf")):
                    if(val==0): # Not possible to reach pacific, atlantic
                        val=0
                        #continue
                    elif(val==1):
                        pacific=True
                    elif(val==2):
                        atlantic=True
                    elif(val==3):
                        pacific=True
                        atlantic=True
                        break
                        
                    continue
                    
                for i in range(0,4):
                    tans=isvalid(ele[0],ele[1],ele[0]+x[i],ele[1]+y[i])
                    if(tans==-2):
                        atlantic=True
                    elif(tans==-1):
                        pacific=True
                    elif(tans==1):
                        if( (ele[0]+x[i],ele[1]+y[i]) not in visited):
                            queue.append([ele[0]+x[i],ele[1]+y[i]])
                            visited.add((ele[0]+x[i],ele[1]+y[i]))
            
            if(pacific and atlantic):
                self.ans.append([r,c])
                self.memo[r][c]=3
            elif(pacific):
                self.memo[r][c]=1
            elif(atlantic):
                self.memo[r][c]=2
            else:
                self.memo[r][c]=0
            
            
            
        
        for i in range(0,len(heights)):
            for j in range(0,len(heights[i])):
                #print("BFS PTS:",i,j)
                bfs(i,j)
        return(self.ans)