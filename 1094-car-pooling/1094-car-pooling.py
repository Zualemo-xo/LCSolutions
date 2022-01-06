class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        #trips=sorted(trips,key=lambda x: x[1])
        #print(trips)
        
        #d=defaultdict(int) taking dict means need to sort so list better for TC
        d=[0]*1001 #constraints 0 <= fromi < toi <= 1000 therefore took 1001 as int list 
        #add at index start and subtract at indexend position   
        for i in trips:
            d[i[1]]+=i[0]
            d[i[2]]-=i[0]
        
        curr,maxcap=0,0
        #heapq.heapify(d)
        for i in d:
            curr+=i
            #print(i,curr)
            if(curr>maxcap):
                maxcap=curr
                if(maxcap>capacity):
                    return(False)
        print(maxcap)
        
        return(True)