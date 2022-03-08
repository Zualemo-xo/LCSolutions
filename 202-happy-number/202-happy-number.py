class Solution:
    def isHappy(self, n: int) -> bool:
        d=defaultdict(int)
        ans=n
        while(ans not in d):
            d[ans]+=1
            ct=0
            for i in str(ans):
                ct+=pow(int(i),2)
            ans=ct
            if(ans==1):
                return(True)
        return(False)
            