class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # see https://www.youtube.com/watch?v=l0YC3876qxg
        nc=n
        ans=1
        if(n<0):
            n*=-1
        while(n):
            
            if(n%2==0):
                x=x*x
                n=n/2
            else:
                ans=x*ans
                n-=1
        if(nc<0):
            ans=1/ans
        return(ans)
                
            
        