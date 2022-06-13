class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        #MEMOIZATION
        self.dp=[]
        for i in t:
            self.dp.append([float("inf")]*len(i))
        
        def helper(row,pos):
            if(pos<0 or pos>row):
                return(float("inf"))
            if(row==len(t)):
                return(0)
            if(self.dp[row][pos]!=float("inf")):
                return(self.dp[row][pos])
            
            else:
                mina=min(helper(row+1,pos), helper(row+1,pos+1) )
                self.dp[row][pos]=mina+t[row][pos]
                return(self.dp[row][pos])
            
            
        return(helper(0,0))



            