class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        #store the overall poured flow in each level for the given 'poured'
        t=[[float(poured)]]
        for i in range(1,query_row+1):
            temp=[]
            for j in range(0,i+1):
                if(j==0 or j==i):
                    x=(t[i-1][0]-1)/2
                    temp.append(x if x>0 else 0) #edge
                    #negative values get added otherwise when cup is not full hence if else
                else:
                    x1=(t[i-1][j-1]-1)/2 if (t[i-1][j-1]-1)/2 >0 else 0
                    x2=(t[i-1][j]-1)/2 if (t[i-1][j]-1)/2 >0 else 0
                    temp.append(x1+x2)
                
            t.append(temp)
        #print(t)
        return(t[query_row][query_glass] if t[query_row][query_glass]<1 else 1)