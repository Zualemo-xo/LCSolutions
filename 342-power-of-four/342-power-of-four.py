class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return(False)
        else:
            num=1
            while(num<n):
                num*=4
            if(num==n):
                return(True)
            else:
                return(False)