class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d=defaultdict(int)
        for i in range(0,len(s)-k+1):
            d[s[i:i+k]]+=1
        #print(d)
        if(len(d)==2**k):
            return(True)
        return(False)