class NumMatrix:
    #prefix sum concept
    def __init__(self, matrix: List[List[int]]):
        self.l=[]
        #prefix sum array
        for i in range(0,len(matrix)):
            for j in range(1,len(matrix[i])):
                matrix[i][j]+=matrix[i][j-1]
        for row in matrix:
            self.l.append(row)
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            if(col1==0):
                ans+=self.l[i][col2]
            else:
                ans=ans-self.l[i][col1-1]+self.l[i][col2]
        return(ans)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)