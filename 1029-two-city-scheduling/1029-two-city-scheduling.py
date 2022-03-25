class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        gain=[]
        d=defaultdict(list)
        # add to city A or B wrt gain
        for i in costs:
            #print(i[0]-i[1])
            gain.append(i[0]-i[1])
            d[i[0]-i[1]].append(i)
        #print(d)
        gain.sort()
        cnt,ans=0,0
        while(cnt<len(costs)/2):
            #print(d[gain[cnt]][0][0])
            ans+=d[gain[cnt]][0][0]
            d[gain[cnt]].pop(0) # to handle [] with equal gain and iterate to next gain pair
            cnt+=1
        while(cnt<len(costs)):
            #print(d[gain[cnt]][0][1])
            ans+=d[gain[cnt]][0][1]
            d[gain[cnt]].pop(0)
            cnt+=1
            
        return(ans)