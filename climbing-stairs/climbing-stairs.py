class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # With list based memoization
        mem=[0]*(n+2)
        def helper(i):
            if(mem[i]!=0):
                return(mem[i])
            if(i>n):
                return(0)
            if(i==n):
                return(1)
            mem[i]=helper(i+1)+helper(i+2)
            return(mem[i])
        return(helper(0))