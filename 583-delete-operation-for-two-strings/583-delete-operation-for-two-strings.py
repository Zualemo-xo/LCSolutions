class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #WORD1-LCS
        #dp[word1][word2]
        dp=[[0 for i in range(0,len(word2)+1)] for j in range(0,len(word1)+1) ]
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if(word1[i-1]==word2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        #print(dp)
        #print(dp[i][j])
        return(len(word1)-dp[i][j]+len(word2)-dp[i][j])