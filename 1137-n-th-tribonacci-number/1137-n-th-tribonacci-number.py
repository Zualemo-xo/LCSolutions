class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        #bottom up w tabluation
        if(n==0 or n==1):
            return(n)
        n1,n2,n3=0,1,1
        for i in range(3,n+1):
            temp=n3
            n3=n1+n2+n3
            n1=n2
            n2=temp
        return(n3)