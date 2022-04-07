import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # to turn minheap implementation of heapq to maxheap, multiply values by -1.
        for i in range(0,len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while(len(stones)>1):
            x1=heapq.heappop(stones)
            x2=heapq.heappop(stones)
            if(x1!=x2):
                #print(x1,x2,x1-x2)
                heapq.heappush(stones,x1-x2)
            print(stones)
        return(0 if len(stones)==0 else -stones[0])