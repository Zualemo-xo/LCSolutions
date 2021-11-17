class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #self.ans=0
        dp=[[0 for i in range(0, n)] for j in range (0, m)]
        # print(dp)
        def helper(currm,currn):
            
            if(currm==m-1 and currn==n-1):
                #self.ans+=1
                return(1)
            elif(currm>m-1 or currn>n-1):
                return(0)
            elif(dp[currm][currn]):
                return(dp[currm][currn])
            #helper(currm+1,currn)
            #helper(currm,currn+1)
            #return(helper(currm+1,currn)+helper(currm,currn+1))
            dp[currm][currn]=helper(currm+1,currn)+helper(currm,currn+1)
            return(dp[currm][currn])
            #print(dp[currm][currn])
        #return(helper(0,0))
        return(helper(0,0))
        
        