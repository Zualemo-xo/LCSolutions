class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x :x[1]) #sort by end value to check if start vals are lesser than it
        arrowcount=1
        endval=points[0][1]
        
        for i in range(0,len(points)):
            if(points[i][0]>endval):
                arrowcount+=1
                endval=points[i][1]
            else:
                arrowcount+=0
                #baloon lies within the endval so it can be shot with one arrow
        return(arrowcount)
        