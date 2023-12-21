class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l = []
        for x,y in points:
            l.append(x)
        l.sort()
        max_diff = 0

        for i in range(1,len(l)):
            max_diff = max(max_diff, l[i] - l[i-1])
        return(max_diff) 


        