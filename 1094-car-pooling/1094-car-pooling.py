class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        #trips=sorted(trips,key=lambda x: x[1])
        #print(trips)
        
        d=defaultdict(int)

        #add at index start and subtract at indexend position   
        for i in trips:
            d[i[1]]+=i[0]
            d[i[2]]-=i[0]
        
        curr,maxcap=0,0
        for i in sorted(d):
            curr+=d[i]
            print(i,curr)
            if(curr>maxcap):
                maxcap=curr
        print(maxcap)
        if(maxcap>capacity):
            return(False)
        return(True)