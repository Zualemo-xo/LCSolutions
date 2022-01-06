class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips=sorted(trips,key=lambda x: x[1])
        #print(trips)
        maxcap=0
        d=defaultdict(int)
        for i in trips:
            d[i[1]]=0
            d[i[2]]=0
        for i in trips:
            for j in d: 
                #print(d[j],j)
                if(i[1]<=j and i[2]>j):
                    d[j]+=i[0]
        for i in d:
            if(d[i]>maxcap):
                maxcap=d[i]
        #print(maxcap)
        if(maxcap>capacity):
            return(False)
        return(True)