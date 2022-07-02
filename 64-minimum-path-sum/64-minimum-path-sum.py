class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        #Memo TC:O(M*N) SC:O((M*N)+m-1+n-1)
        m=len(grid)
        n=len(grid[0])
        memo=[[-1 for i in range(n)] for j in range(m) ]
        def solve(m,n):
            #Base 
            if(memo[m][n]!=-1):
                return(memo[m][n])
            if(m<0 or n<0 ):
                return(float("inf"))
            elif(m==0 and n==0):
                return(grid[m][n])
            
            up=solve(m-1,n)
            left=solve(m,n-1)
            ans=grid[m][n]+min(up,left)
            memo[m][n]=ans
            return(memo[m][n])
            
            
        x=solve(m-1,n-1)
        print(memo)
        return(x)
                    