class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Memo TC:O(M*N) SC:O((M*N)+m-1+n-1)
        memo=[[-1 for i in range(n)] for j in range(m) ]
        def solve(m,n):
            #Base 
            if(memo[m][n]!=-1):
                return(memo[m][n])
            if(m<0 or n<0 ):
                return(0)
            elif(m==0 and n==0):
                return(1)
            
            up=solve(m-1,n)
            left=solve(m,n-1)
            ans=up+left
            memo[m][n]=ans
            return(memo[m][n])
            
            
        return(solve(m-1,n-1))