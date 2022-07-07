import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Heap
        l=[]
        heapq.heapify(l)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                heapq.heappush( l, grid[i][j] )

        
        self.n=len(grid)
        def isvalid(x,y,rainlevel):
            #print("SHT:",x,y,rainlevel)
            if(x>=0 and y>=0 and x<self.n and y<self.n and grid[x][y]<=rainlevel):
                return(True)
            return(False)

        def dij(x,y,rainlevel):
            #4 directionally adjacent
            p1=[0,0,-1,1]
            p2=[1,-1,0,0]
            if(isvalid(x,y,rainlevel)==False): #0,0 coordinate might be inaccessible at start
                return(False)
            else:
                queue=[(x,y)]
                heapq.heapify(queue)
            
            visited=set()
            while(len(queue)!=0):
                ele=heapq.heappop(queue)
                if(ele in visited):
                    continue
                r,c=ele[0],ele[1]
                visited.add((r,c))
                #print(r,c,rainlevel)
                
                if(r==self.n-1 and c==self.n-1): #We have reached n-1,n-1
                    return(True)
                #Else continue bfs
                for i in range(4):
                    if( isvalid(r+p1[i],c+p2[i],rainlevel) ):
                        #print("rhy")
                        heapq.heappush(queue, (r+p1[i],c+p2[i]) )
            return(False) # we have exhausted elements in a queue and have not reached n-1,n-1
            
        #Main fn
        # Traverse thru heapq elements from smallest to greatest to find min ans optimally
        while(len(l)>0):
            rainlevel=heapq.heappop(l)
            canCross=dij(0,0,rainlevel)
            if(canCross):
                return(rainlevel)

            
            
            
        