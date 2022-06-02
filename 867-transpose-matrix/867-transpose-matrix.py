class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m=len(matrix),len(matrix[0])
        #ans[m][n]
        ans=[[0 for i in range(n)] for j in range(m)]
        #traverse original array, insert vals into transpose
        for i in range(n):
            for j in range(m):
                ans[j][i]=matrix[i][j]
        return(ans)