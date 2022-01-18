class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans=[]
        mem = [[0 for i in range(rowIndex+1)] for j in range(rowIndex+1)]
        def helper(row,col):
            if(mem[row][col]!=0):
                return(mem[row][col])
            if(row==0 or row==1 or col==0 or col==row):
                return(1)
            else:
                mem[row-1][col-1]=helper(row-1,col-1)
                mem[row-1][col]=helper(row-1,col)
                return(mem[row-1][col-1]+mem[row-1][col])
        
        for i in range(0,rowIndex+1):
            ans.append(helper(rowIndex,i))
        return(ans)