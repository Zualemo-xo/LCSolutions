class Solution:
    def canPartition(self, A):
        #bottum up tabulation
        B=sum(A)
        if(B%2!=0):
            return(False)
        B=B//2
        dp=[[False for i in range(0,B+1)] for j in range(0,len(A)+1)]
            #print(B)
            #base case
        for i in range(0,len(A)+1):
            for j in range(0,B+1):
                if(j==0):
                    dp[i][j]=True  
                elif(i==0):
                    dp[i][j]=False
                      # code here 

        for i in range(1,len(A)+1):
            for j in range(1,B+1):
                if(A[i-1]>j):
                    dp[i][j]=dp[i-1][j] 
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-A[i-1]]
        return(dp[len(A)][B])
