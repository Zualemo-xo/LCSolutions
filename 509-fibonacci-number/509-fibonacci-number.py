class Solution:
    def fib(self, n: int) -> int:
        if(n<2):return(n)
        x1,x2=0,1
        for i in range(2,n+1):
            temp=x2
            x2+=x1
            x1=temp
        return(x2)