class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #Day 365 wow

        n,m=len(matrix),len(matrix[0])
        for z in range(0,n):
            for i in range(0,m):
                initial=matrix[z][i]
                j=i+1
                k=z+1
                while(j<m and k<n):
                    if(matrix[k][j]==initial):
                        j+=1
                        k+=1

                    else:
                        return(False)
        return(True)
        