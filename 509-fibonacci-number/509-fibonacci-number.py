class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #bottom up w tabluation
        if(n==0):
            return(0)
        n1,n2=0,1
        for i in range(2,n+1):
            temp=n2
            n2=n1+n2
            n1=temp
        return(n2)
            
                