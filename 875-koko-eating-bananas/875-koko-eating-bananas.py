class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minb,maxb=1,max(piles)
        
        while(minb<maxb):
            mid=(minb+maxb)//2
            hr=0
            for i in range(0,len(piles)):
                hr+=math.ceil(piles[i]/mid)
                #print(hr,mid)
            if(hr<=h):
                maxb=mid   
            else:
                minb=mid+1
        return(maxb)