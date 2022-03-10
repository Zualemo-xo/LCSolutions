#User function Template for python3

class Solution:
    def isSubsetSum (self, n, A, B):
        dp=[[False for i in range(0,B+1)] for j in range(0,len(A)+1)]
        #print(dp)
        for i in range(0,len(A)+1):
            for j in range(0,B+1):
                if(j==0):
                    dp[i][j]=True  
                elif(i==0):
                    dp[i][j]=False
                      # code here 
        #print(dp)
        for i in range(1,len(A)+1):
            for j in range(1,B+1):
                if(A[i-1]>j):
                   dp[i][j]=dp[i-1][j] 
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-A[i-1]]
        return(dp[len(A)][B])
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends