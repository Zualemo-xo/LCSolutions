class Solution:
    def longestCommonSubsequence(self, S1: str, S2: str) -> int:
        @cache
        def helper(n,m):
            #base
            if(n==-1 or m==-1):
                return(0)
            #choice diag
            if(S1[n]==S2[m]):
                return(1+helper(n-1,m-1))

            else:
                return(max(helper(n-1,m),helper(n,m-1)))

        n,m=len(S1),len(S2)   
        return(helper(n-1,m-1))
        