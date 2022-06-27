class Solution(object):
    def maxScore(self, points, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        #sliding window of size n-k to see what elements to not consider
        
        sw=deque([])
        maxl=len(points)-k
        if(maxl==0): #EDGE C
            return(sum(points))
        
        cursum=0
        minsum=float("inf")
        for i in range(0,len(points)):
            if(len(sw)<maxl):
                sw.append(points[i])
                cursum+=points[i]
                
            elif(len(sw)==maxl):
                minsum=min(cursum,minsum)
                ele=sw.popleft()
                cursum-=ele
                sw.append(points[i])
                cursum+=points[i]
                
        minsum=min(cursum,minsum)
        return(sum(points)-minsum)
                
                
            
        
        
        
        