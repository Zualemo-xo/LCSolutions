class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #P1 CREATING TABULATION
        
        #dp[str1][str2]
        #WHILE CREATING dp array ensure 1 extra row is created to accomodate for null row and column
        dp=[[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
        for i in range(1,len(str1)+1): #start iteration from 1 to leave null row and column as 0
            for j in range(1,len(str2)+1):
                if(str1[i-1]==str2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        #print(dp)
            
        
        #P2 BACKTRACT THRU DP TABULATION FOR FINAL ANSWER STRING
        i,j=len(str1),len(str2)
        ans=""
        while(i>0 and j>0):
            if(str1[i-1]==str2[j-1]):
                ans+=str1[i-1]
                i-=1
                j-=1
            else:
                if(dp[i][j-1]>dp[i-1][j]):
                    ans+=str2[j-1]
                    j-=1
                else:
                    ans+=str1[i-1]
                    i-=1
        #print(ans)
        #Print the lingering letters
        while(i>0):
            ans+=str1[i-1]
            i-=1
        while(j>0):
            ans+=str2[j-1]
            j-=1
        return(ans[::-1])
                