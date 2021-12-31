class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        ll=0
        ul=0
        intervals.sort()
        intervals.append([float("inf"),float("inf")])
        #for i in range(0,len(intervals)-1):
        while(ul<len(intervals)-1):
            if(intervals[ul][1]>intervals[ul+1][1]):
                intervals[ul+1][1]=intervals[ul][1]
            elif(intervals[ul][1]>=intervals[ul+1][0]):
                ul+=1
            elif(intervals[ul][1]<intervals[ul+1][0]):
                ans.append([intervals[ll][0],intervals[ul][1]])
                ul+=1
                ll=ul
            
        return(ans)