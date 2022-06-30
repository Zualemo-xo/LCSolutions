class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        #Recursion with memoization
        #memo[egg][floor]
        memo=[[-1 for i in range(n+1)] for j in range(2+1)]
        def solve(e,f):
            #Memo
            if(memo[e][f] != -1):
                return(memo[e][f])
            #Base
            if(e==0 or e==1):
                return(f)
            if(f==0 or f==1):
                return(f)
            
            
            #MCM
            ans=float("inf")
            for k in range(1,f):
                temp=1+max(solve(e-1,f-k),solve(e,k-1))
                ans=min(ans,temp)
            memo[e][f]=ans
            return(ans)
        
        return(solve(2,n))
        