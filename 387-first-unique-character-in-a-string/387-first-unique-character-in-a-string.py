class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        ans=-1
        for i in d:
            if(d[i]==1):
                ans=i
                break
        if(ans==-1):
            return(-1)
        else:
            return(s.index(ans))
                
            