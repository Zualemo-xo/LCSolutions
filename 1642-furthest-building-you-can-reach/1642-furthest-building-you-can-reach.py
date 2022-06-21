import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        pq=[]
        heapq.heapify(pq) #Holds the ladder values
        for i in range(0,len(heights)-1):
            diff=heights[i]-heights[i+1]
            #print("sds:",diff,bricks)
            if(diff<0):
                #print(diff,bricks,pq)
                heapq.heappush(pq,abs(diff))
                #print(diff,bricks,pq)
                if(len(pq)>ladders):
                    bricks-=heapq.heappop(pq)
            if(bricks<0):
                return(i)
        return(len(heights)-1)
                
        