class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #TC : O(M+N) SC:O(1)
        row,col=0,len(matrix[0])-1
        while(row<len(matrix) and col>=0):
            if(matrix[row][col]>target):
                col-=1
            elif(matrix[row][col]<target):
                row+=1
            else:
                return(True)
        return(False)