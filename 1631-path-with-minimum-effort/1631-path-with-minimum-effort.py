import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Dijixtra
        #heapq will have a tuple defined as (difference,row,col)
        l=[]
        heapify(l)
        heapq.heappush(l,(0,0,0)) #sort heap wrt 'difference'
        visited=set()
        rlen,clen=len(heights),len(heights[0])
        while(heapq!=None):
            dist,x,y=heapq.heappop(l)
            #print(l)
            #print(dist,x,y)
            if((x,y) not in visited): #to avoid infinite loops 
                visited.add((x,y))
                if(x==rlen-1 and y==clen-1):
                    return(dist)
                #select maximum absolute difference in heights between two consecutive cells of the route--- using max(old_dist,new_abs_diff) 
                if(y<clen-1):
                    heapq.heappush( l,( max(dist,abs(heights[x][y]-heights[x][y+1])),x,y+1 ) )  #move right
                if(y>0):
                    heapq.heappush( l,( max(dist,abs(heights[x][y-1]-heights[x][y])),x,y-1 ) ) #move left
                if(x<rlen-1):
                    heapq.heappush( l,( max(dist,abs(heights[x+1][y]-heights[x][y])),x+1,y ) ) #move down
                if(x>0):
                    heapq.heappush( l,( max(dist,abs(heights[x-1][y]-heights[x][y])),x-1,y ) ) #move up
                
        