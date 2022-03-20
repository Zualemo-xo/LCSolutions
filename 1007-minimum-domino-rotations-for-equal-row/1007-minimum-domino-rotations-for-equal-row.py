class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        #Greedy
        #Find out max occuring val in top and bottom, chk with alt case if they exist or not
        d1,d2=defaultdict(int),defaultdict(int)
        for i in tops:
            d1[i]+=1
        for i in bottoms:
            d2[i]+=1
        maxt,maxb=-1,-1
        p1,p2=-1,-1
        for i in d1:
            if(d1[i]>p1):
                p1=d1[i]
                maxt=i
        for i in d2:
            if(d2[i]>p2):
                p2=d2[i]
                maxb=i
        
        cnt=0
        imp=False
        for i in range(0,len(tops)):
            if(tops[i]!=maxt):
                if(bottoms[i]!=maxt):
                    imp=True
                    break
                else:
                    cnt+=1
        #if(imp==False):
            #return(cnt)
        cnt1=0
        for i in range(0,len(bottoms)):
            if(bottoms[i]!=maxb):
                if(tops[i]!=maxb):
                    if(imp==False):
                        return(cnt) #top count returned, as bottom is impossiblwe
                    else:
                        return(-1)
                else:
                    cnt1+=1
        if(imp==True): #top is impossible to arrange , hence bottom cnt retuerned
            return(cnt1)
        else:
            return(min(cnt,cnt1))
                
                