class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(accumulated_ans,r,c):
            #exit case
            if(r==n):
                nq=0
                for row in accumulated_ans:
                    nq+=sum(row)
                if(nq==n): # if there are N QUEENS on the board
                    #build final ans
                    tans=[]
                    for i in accumulated_ans:
                        tstr=""
                        for j in i:
                            if(j==0):
                                tstr+="."
                            else:
                                tstr+="Q"
                        tans.append(tstr)
                    if(tans not in self.ans):
                        self.ans.append(tans)
                return
            #chk for col elements for row 'r'    
            for j in range(0,n):

                #Check if adding a Q here will be valid
                isvalid=True
                sumz=0
                sumz+=sum(accumulated_ans[r]) #rowsum
                for x in range(0,len(accumulated_ans)):
                    sumz+=accumulated_ans[x][j]     #col sum
                    
                #diagonals
                for x in range(0,n):
                    for y in range(0,n):
                        if(r-j==x-y or r+j==x+y):
                            sumz+=accumulated_ans[x][y]

                if(sumz>0):
                    isvalid=False
                    
                #proceed for backtracking based on isvalid
                if(isvalid):
                        
                    accumulated_ans[r][j]=1
                    backtrack(accumulated_ans,r+1,j)
                    accumulated_ans[r][j]=0 #backtrack

        
        l=[[0 for i in range(n)] for j in range(n)]
        self.ans=[]
        backtrack(l,0,0)
        return(self.ans)