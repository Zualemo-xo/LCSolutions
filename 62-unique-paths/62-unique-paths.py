class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Bottum Up
        #Memo TC:O(M*N) SC:O((M*N))
        dp=[[0 for i in range(n+1)] for j in range(m+1) ]
        for i in range(0,m):
            for j in range(0,n):
                if(i==0 or j==0):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return(dp[i][j])
                    
        
        