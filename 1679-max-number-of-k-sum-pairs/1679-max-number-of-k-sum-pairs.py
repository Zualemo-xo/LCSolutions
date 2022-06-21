class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        ans=0
        print(d)
        for i in nums:
            #print(d)
            if(k-i in d):
                #print(i,k/2)
                if(i==k/2):
                    ans+=math.floor(d[i]/2)
                    #print(ans)
                    d[i]=0
                else:
                    #print(min(d[i],d[k-i]))
                    mina=min(d[i],d[k-i])
                    ans+=mina
                    d[i]-=mina
                    d[k-i]-=mina
                    #print(i,k-i,d[k-i])
                    #print(ans,i,d[i],k-i,d[k-i])

        return(ans)
                