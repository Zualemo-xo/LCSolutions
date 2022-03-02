class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1):
            return(1)
        s1,s2=1,2
        for i in range(3,n+1):
            temp=s2
            s2=s1+s2
            s1=temp
        return(s2)
        