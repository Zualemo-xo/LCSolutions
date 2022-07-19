class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp=[[1]]
        for i in range(1,n):
            temp=[]
            for j in range(0,i+1):
                if(j==0):
                    temp.append(dp[i-1][j])
                elif(j==i):
                    temp.append(dp[i-1][j-1])
                else:
                    temp.append(dp[i-1][j-1]+dp[i-1][j])
            dp.append(temp)
        return(dp)
        