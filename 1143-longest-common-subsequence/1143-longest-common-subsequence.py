class Solution:
    def longestCommonSubsequence(self, S1: str, S2: str) -> int:
        @cache
        def helper(n,m):
            #base
            if(n==-1 or m==-1):
                return(0)
            #choice diag
            if(S1[n]==S2[m]):
                x=1+helper(n-1,m-1)
                self.maxn=max(self.maxn,x)
                return(x)

            else:
                return(max(helper(n-1,m),helper(n,m-1)))

        n,m=len(S1),len(S2)   
        self.maxn=0
        helper(n-1,m-1)
        return(self.maxn)
        