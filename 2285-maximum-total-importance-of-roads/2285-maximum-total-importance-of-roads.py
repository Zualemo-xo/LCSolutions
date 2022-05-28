class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(int)
        #Count interconnectivity of roads
        for i in roads:
            d[i[0]]+=1
            d[i[1]]+=1
        xd=sorted(d.items(),key=lambda x:x[1],reverse=True)
        #print(xd)
        #Assign values from n...0
        assig=defaultdict(int)
        for i in xd:
            assig[i[0]]=n
            n-=1
        #print(assig)
        #Final ans count of importance
        ans=0
        for i in roads:
            ans+=assig[i[0]]+assig[i[1]]
        return(ans)