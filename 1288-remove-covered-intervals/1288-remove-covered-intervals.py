class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt=0
        for i in range(0,len(intervals)):
            for j in range(0,len(intervals)):
                #print(intervals[i],intervals[j])
                if(intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1] and i!=j):
                    #print(intervals[i],intervals[j])
                    cnt+=1
                    break
        return(len(intervals)-cnt)