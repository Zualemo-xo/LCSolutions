class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted=defaultdict(int)
        trust1=defaultdict(int)
        if(n==1):
            return(1)
        for i in trust:
            trust1[i[0]]+=1
            trusted[i[1]]+=1
            
        for v,k in trusted.items():
            if(k==n-1 and v not in trust1):
                return(v)
        return(-1)