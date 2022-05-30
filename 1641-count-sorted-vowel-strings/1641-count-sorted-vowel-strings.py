class Solution:
    def countVowelStrings(self, n: int) -> int:
        # The pattern of how n=3 depends on n=2's next vowel values by summing up the respective 'j' values was observered on pen and paper, leading t0 line 8.
        #dp[n][5]
        dp=[[1 for i in range(5)] for j in range(n)]
        for i in range(1,n):
            for j in range(0,5):
                dp[i][j]=sum(dp[i-1][j:])
        return(sum(dp[n-1]))
        
                