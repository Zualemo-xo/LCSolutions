class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def isValid(x,y,oldcolor):
            if(x>=0 and y>=0 and x<len(image) and y<len(image[0]) and image[x][y]==oldcolor ):
                return(True)
            return(False)
        
        # BFS
        queue=deque([[sr,sc]])
        visited=set()
        marked=[]
        x=[0,0,-1,1]
        y=[-1,1,0,0]
        #Find values connected to sr,sc with same color
        while(len(queue)!=0):
            #print(queue)
            r,c=queue.popleft()
            if((r,c) in visited):
                continue
            else:
                visited.add((r,c))

            for i in range(0,4):
                if(isValid( r+x[i],c+y[i],image[r][c] )):
                    queue.append([ r+x[i],c+y[i] ])
        #print(visited)
        #Iterate and mark with newcvolor
        for r,c in visited: 
            image[r][c]=color
        return(image)
        