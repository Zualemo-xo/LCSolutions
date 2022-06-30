class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if(image[sr][sc]==color): # Both initial and final colors are samje , prevents infinite loop
            return(image)
        
        def isValid(x,y,oldcolor):
            if(x>=0 and y>=0 and x<len(image) and y<len(image[0]) and image[x][y]==oldcolor ):
                return(True)
            return(False)
        
        # BFS
        queue=deque([[sr,sc]])
        oldcolor=image[sr][sc]
        visited=set()
        marked=[]
        x=[0,0,-1,1]
        y=[-1,1,0,0]
        #Find values connected to sr,sc with same color
        
        while(len(queue)!=0):

            r,c=queue.popleft()
            for i in range(0,4):

                if(isValid( r+x[i],c+y[i],oldcolor )):
                    queue.append([ r+x[i],c+y[i] ])
            image[r][c] = color #We directly mark to avoid using visited array
            
        # We can do it without visited and 2nd iteration by directly changing value after checking all 4 colors near it and adding into queue
        # #print(visited)
        # #Iterate and mark with newcvolor
        # for r,c in visited: 
        #     image[r][c]=color
        return(image)
        