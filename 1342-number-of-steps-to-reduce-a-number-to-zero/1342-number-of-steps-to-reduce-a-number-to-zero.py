class Solution:
    def numberOfSteps(self, num: int) -> int:
        #Bit Manipulation: to remove 1 at the left most--1 turn ,other 1 -- 2 turns, 0 -- 1 turns
        cnt=0
        while(num!=0):
            if(num==1): #Exception case
                cnt+=1
                break
            x=num&1
            cnt=cnt+2 if x==1 else cnt+1
            num>>=1
        return(cnt)