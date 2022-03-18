class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[[0 for i in range(0,amount+1)] for j in range(0,len(coins)+1)]
        #print(dp)
        
        #Initialization
        #amount=0 ,then 1 possibility
        for i in range(0,len(coins)+1):
            dp[i][0]=1
            
        #tabulation
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if(coins[i-1]<=j):
                    dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return(dp[-1][-1])