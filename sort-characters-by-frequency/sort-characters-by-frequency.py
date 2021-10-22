class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        ans=""
        d=sorted(d.items(), key =lambda kv:kv[1],reverse=True)
        #print(d)
        for key,val in d:
            ans+=key*val
        return(ans)