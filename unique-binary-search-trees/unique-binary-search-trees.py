class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        uniquebst=[0,1]
        for i in range(2,n+2):
            uniquebst.append(0)
            for j in  range(1,i+1):
                lhtree=j-1
                rhtree=i+1-j
                uniquebst[i]+=uniquebst[lhtree]*uniquebst[rhtree]
        #print(uniquebst)
        return(uniquebst[n+1])