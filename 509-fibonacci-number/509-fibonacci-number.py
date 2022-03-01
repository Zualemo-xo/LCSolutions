class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #top down w memoization
        d=defaultdict(int)
        def helper(n):
            if(n==0 or n==1):
                return(n)
            if(n in d):
                return(d[n])
            else:
                d[n]=helper(n-1)+helper(n-2)
            return(d[n])
        return(helper(n))
            
                