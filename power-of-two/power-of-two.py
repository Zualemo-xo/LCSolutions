class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<0):
            return(False)
        n=bin(n)[2:]
        cnt=0
        for i in n:
            if(i=="1"):
                cnt+=1
        if(cnt==1):
            return(True)
        return(False)